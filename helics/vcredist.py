# -*- coding: utf-8 -*-
import logging
import os
import urllib

logger = logging.getLogger(__name__)

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def filename_from_url(url):
    """Return the filename from a given url."""
    return os.path.basename(urllib.parse.urlparse(url).path)


def download_file(url, filepath):
    """Download the file from url and store it in the given filepath."""

    with urllib.request.urlopen(url) as f:
        content = f.read().decode("utf-8")

    with open(filepath, "wb") as f:
        f.write(content)


class VcRedist(object):
    name = "vcredist"
    description = "Visual studio redistributable packages"
    default = "2015"

    install_params = {
        "2015": "/passive /norestart",
    }

    exes = [
        {"version": "2015", "arch": "amd64", "url": "https://aka.ms/vs/16/release/vc_redist.x64.exe"},
        {"version": "2015", "arch": "x86", "url": "https://aka.ms/vs/16/release/vc_redist.x86.exe"},
    ]

    def __init__(self, version="2015", arch="amd64"):

        self.exe = None
        # Locate the matching installer.
        for exe in self.exes:
            if exe["version"] != self.version:
                continue

            if exe["arch"] != self.arch:
                continue

            self.exe = exe
            break
        else:
            if self.exes:
                logger.error("Could not find the correct installer!")
                raise NotImplementedError("Could not find the correct installer!")

        # Download the dependency (if there is any to download).
        if self.exe:
            self.download_and_run()

    def download_and_run(self):

        url = self.exe["url"]
        filename = filename_from_url(url)
        filepath = os.path.join(CURRENT_DIRECTORY, filename)

        download_file(url, filepath)

        cmd = "{} {}".format(os.path.join(CURRENT_DIRECTORY, filepath), " /install /quiet /norestart")
        os.system(cmd)
