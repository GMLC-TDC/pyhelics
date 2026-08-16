# Copyright (c) 2017-2026,
# Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Energy
# Innovation LLC. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause

import helics as h
import time

broker = h.helicsCreateBroker("zmq", "", "-f 2 --loglevel=trace")

while h.helicsBrokerIsConnected(broker):
    time.sleep(1)
