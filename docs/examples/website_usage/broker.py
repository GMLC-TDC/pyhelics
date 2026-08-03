import helics as h
import time

broker = h.helicsCreateBroker("zmq", "", "-f 2 --loglevel=trace")

while h.helicsBrokerIsConnected(broker):
    time.sleep(1)