# -*- coding: utf-8 -*-
"""
HELICS command line interface
"""

import json
import os
import io
import shlex
import subprocess
import collections
import platform
import urllib.request
import logging
from ._version import __version__
from .status_checker import CheckStatusThread, HELICSRuntimeError

import click
import pathlib

from typing import Union

from .utils import echo, info, warn, error

HELICS_CLI_SERVER_API = "http://127.0.0.1:5000/api"

logger = logging.getLogger(__name__)


def _get_version():
    try:
        import helics as h

        helics_version = "Python HELICS version {}\n\nHELICS Library version {}".format(h.__version__, h.helicsGetVersion())
    except ImportError:
        helics_version = "Python `helics` package not installed. Install using `pip install helics --upgrade`."
    try:
        import helics_apps as ha

        helics_apps_version = "HELICS Apps version {}".format(ha.__version__)

    except ImportError:
        helics_apps_version = ""

    try:
        import helics as h
        import helics_apps as ha

        if not h.helicsGetVersion().startswith(ha.__version__.strip("v")):
            echo("`helics` and `helics-apps` versions don't match. You may want to run `pip install helics helics-apps --upgrade`.")
    except ImportError:
        pass

    try:
        import flask
    except ImportError:
        echo('helics-cli\'s web interface is not installed. You may want to run `pip install "helics[cli]"`.')

    try:
        import sqlalchemy
    except ImportError:
        echo('helics-cli\'s observer functionality is not installed. You may want to run `pip install "helics[cli]"`.')

    return """{}

{}

{}
""".format(
        __version__, helics_version, helics_apps_version
    ).strip()


VERSION = _get_version()


@click.group()
@click.version_option(VERSION, "--version")
@click.option("--verbose", "-v", count=True)
@click.pass_context
def cli(ctx, verbose):
    """
    HELICS Runner command line interface
    """
    ctx.obj = {}
    ctx.obj["verbose"] = verbose


@cli.command()
@click.option(
    "--open/--no-open",
    is_flag=True,
    default=True,
    show_default=True,
    help="Open browser on startup",
)
def server(open: bool):
    """
    Run helics web server to access web interface
    """
    import webbrowser
    from . import flaskr

    if open:
        webbrowser.open("http://127.0.0.1:5000", 1)
    flaskr.run()


@cli.command()
@click.option("--db-folder", prompt="path to database folder", type=click.Path(exists=True, file_okay=False, writable=True, path_type=pathlib.Path))
def observer(db_folder: pathlib.Path):
    """
    Run helics observer and write data to sqlite file
    """
    from .observer import HelicsObserverFederate

    o = HelicsObserverFederate(folder=db_folder)
    o.run()


@cli.command()
@click.option(
    "--path",
    required=True,
    type=click.Path(file_okay=True, exists=True),
    help="Path to profile.txt that describes profiling results of a federation",
)
@click.option(
    "--invert",
    is_flag=True,
    default=True,
    help="Invert plot",
)
@click.option("--save", prompt=True, prompt_required=False, type=click.Path(), default=None, help="Path to save the plot")
def profile_plot(path, save, invert):
    """
    Plot profiler output using matplotlib
    """
    from . import profile as p

    p.plot(p.profile(path, invert), save=save, kind="realtime")


from dataclasses import dataclass


@dataclass
class Job:
    name: str
    process: subprocess.Popen
    file: str


@dataclass
class Output:
    name: str
    file: Union[io.TextIOWrapper, None]


def fetch(url, data={}, method="POST"):
    r = urllib.request.Request("{}{}".format(HELICS_CLI_SERVER_API, url), method=method)
    r.add_header("Content-Type", "application/json; charset=utf-8")
    bytes = json.dumps(data).encode("utf-8")
    r.add_header("Content-Length", str(len(bytes)))
    try:
        with urllib.request.urlopen(r, bytes) as response:
            return json.loads(response.read().decode(response.info().get_param("charset") or "utf-8"))
    except Exception as e:
        logger.exception("Unable to post to helics-cli server: {}".format(e))


@cli.command()
@click.option(
    "--path",
    required=True,
    type=click.Path(file_okay=True, exists=True),
    help="Path to config.json that describes how to run a federation",
)
@click.option("--silent", is_flag=True)
@click.option("--connect-server", is_flag=True)
@click.option("--no-log-files", is_flag=True, default=False)
@click.option("--no-kill-on-error", is_flag=True, default=False, help="Do not kill all federates on error")
def run(path, silent, connect_server, no_log_files, no_kill_on_error):
    """
    Run HELICS federation
    """

    r = urllib.request.Request("{}/health".format(HELICS_CLI_SERVER_API))

    helics_server_available = False
    try:
        if connect_server:
            with urllib.request.urlopen(r) as response:
                helics_server_available = (
                    json.loads(response.read().decode(response.info().get_param("charset") or "utf-8")).get("status", None) == 200
                )
    except Exception:
        warn("Unable to connect to helics-cli web server")
        helics_server_available = False

    log = not no_log_files
    kill_on_error = not no_kill_on_error
    path_to_config = os.path.abspath(path)
    path = os.path.dirname(path_to_config)

    if not os.path.exists(path_to_config):
        info(
            "Unable to find file `config.json` in path: {path_to_config}".format(path_to_config=path_to_config),
        )
        return None

    with open(path_to_config) as f:
        config = json.loads(f.read())

    if not silent:
        info("Running federation: {name}".format(name=config["name"]))

    if "broker" in config.keys() and config["broker"] is not False:
        if not silent:
            info(
                "Adding auto broker (i.e. `helics_broker -f{f}`) to helics-cli subprocesses.".format(f=len(config["federates"])),
                blink=True,
            )
        config["federates"].append(
            {"directory": ".", "exec": "helics_broker -f{}".format(len(config["federates"])), "host": "localhost", "name": "broker"}
        )

    names = [c["name"] for c in config["federates"]]
    if len(set(n for n in names)) != len(config["federates"]):
        error("Repeated names found in runner.json federates.", blink=True)
        for n, c in [(item, count) for item, count in collections.Counter(names).items() if count > 1]:
            info('Found name "{}" {} times'.format(n, c))
        return -1

    if helics_server_available:
        fetch("/runner/file/name", {"name": os.path.basename(path_to_config)})
        fetch("/runner/file/folder", {"folder": os.path.dirname(path_to_config)})

    process_list = []
    output_list = []
    for f in config["federates"]:
        if not silent:
            info(
                "Running federate {name} as a background process".format(name=f["name"]),
            )

        fname = os.path.abspath(os.path.join(path, "{}.log".format(f["name"])))
        if log is True:
            o = Output(fname, open(fname, "w"))
        else:
            o = Output(fname, None)

        try:
            directory = os.path.join(path, f["directory"])

            env = dict(os.environ)
            if "env" in f:
                for k, v in f["env"].items():
                    env[k] = v
            p = subprocess.Popen(
                shlex.split(f["exec"]),
                cwd=os.path.abspath(os.path.expanduser(directory)),
                stdout=o.file,
                stderr=o.file,
                env=env,
            )

            p = Job(name=f["name"], process=p, file=o.name)

        except FileNotFoundError as e:
            raise click.ClickException("FileNotFoundError: {}".format(e))
        process_list.append(p)
        if o.file is not None:
            output_list.append(o)

    t = CheckStatusThread(process_list, kill_on_error, helics_server_available)

    try:
        t.start()
        if not silent:
            info(
                "Waiting for {} processes to finish ...".format(len(process_list)),
            )
        for p in process_list:
            p.process.wait()
    except KeyboardInterrupt:
        warn("User interrupted processes. Terminating safely ...")
        for o in output_list:
            o.file.close()
        for p in process_list:
            p.process.kill()
    except Exception as e:
        click.echo("")
        error(f"{e}. Terminating ...")
        if kill_on_error:
            for o in output_list:
                o.file.close()
            for p in process_list:
                p.process.kill()
    finally:
        for p in process_list:
            t.status(p)
            if p.process.returncode != 0 and p.process.returncode != -9 and p.process.returncode is not None:
                error("Process {} exited with return code {}".format(p.name, p.process.returncode))
                if os.path.exists(p.file):
                    with open(p.file) as f:
                        warn("Last 10 lines of {}.log:".format(p.name), blink=False)
                        print("...")
                        for line in f.readlines()[-10:]:
                            print(line, end="")
                        print("...")

    info("Done.")


@cli.command()
def kill_all_brokers():
    """
    Kill all brokers
    """
    name = "helics_broker"

    if platform.system().lower().startswith("windows"):
        # windows OS
        if not name.endswith(".exe"):
            name = name + ".exe"
        os.system("taskkill /f /im {}".format(name))
        # os.system(r"start /b pcs.exe 2>&1")
        # with os.popen("tasklist | findstr \"pcs.exe\"") as f:
        #     temp_content = f.read()
        # if len(temp_content) == 0:
        #     pass
    else:
        if name.endswith(".exe"):
            name = name.replace(".exe", "")
        os.system("killall -9 {} 2>&1".format(name))


@cli.command()
def list_brokers():
    """
    List all brokers that are running
    """

    if platform.system().lower().startswith("windows"):
        # windows OS
        with os.popen('tasklist | findstr "helics_broker.exe"') as f:
            data = f.read()
        if len(data) != 0:
            print(data)

    else:
        cmd = "ps aux"
        p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        p.wait()
        out, _ = p.communicate()
        for line in out.decode("utf-8").splitlines():
            if "helics_broker" in line:
                print(line)


if __name__ == "__main__":
    cli()
