import os
import subprocess
import sys

from ._build import PYHELICS_INSTALL

BIN_DIR = os.path.join(PYHELICS_INSTALL, 'bin')

def _program(name, args):
    return subprocess.call([os.path.join(BIN_DIR, name)] + args)

def helics_app():
    raise SystemExit(_program('helics_app', sys.argv[1:]))

def helics_broker():
    raise SystemExit(_program('helics_broker', sys.argv[1:]))

def helics_broker_server():
    raise SystemExit(_program('helics_broker_server', sys.argv[1:]))

def helics_player():
    raise SystemExit(_program('helics_player', sys.argv[1:]))

def helics_recorder():
    raise SystemExit(_program('helics_recorder', sys.argv[1:]))
