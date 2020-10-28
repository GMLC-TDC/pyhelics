#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

import helics as h


def create_broker(number_of_federates: int = 2):

    brokerinitstring = "-f 2"

    print("Creating Broker")
    broker = h.helicsCreateBroker("zmq", "", brokerinitstring)
    print("Created Broker")

    if broker.is_connected():
        print("Broker created and connected")

    print(broker)

    while broker.is_connected():
        time.sleep(1)

    broker.disconnect()


def print_help():
    print(
        """
python broker.py {n}

n: int - number of federates you want to have connect to the broker
"""
    )


def main():
    try:
        number_of_federates = int(sys.argv[1])
    except Exception:
        print_help()
        sys.exit(-1)

    if len(sys.argv) != 2:
        print("Number of arguments must be exactly 2. Check documentation for broker.py")
        sys.exit(-1)

    create_broker(number_of_federates)
