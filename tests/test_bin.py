# Copyright (c) 2017-2026,
# Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Energy
# Innovation LLC. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause

import shutil
import subprocess
import sys
import time

import pytest as pt


@pt.mark.skipif(sys.platform == "win32", reason="no exec on Windows")
def test_killing_broker_script_kills_broker():
    p = subprocess.Popen([shutil.which("helics_broker"), "-f1", "--name=killtestbroker"])
    time.sleep(1)
    p.kill()
    p.wait()
    time.sleep(0.5)
    leftover = subprocess.run(["pgrep", "-f", "killtestbroker"], capture_output=True)
    subprocess.run(["pkill", "-9", "-f", "killtestbroker"])
    assert leftover.returncode != 0, "helics_broker outlived its console script"
