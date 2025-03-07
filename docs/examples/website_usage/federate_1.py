import time
import helics as h
from math import pi

fedinfo = h.helicsCreateFederateInfo()

h.helicsFederateInfoSetCoreName(fedinfo, "Federate1")
h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")
h.helicsFederateInfoSetCoreInitString(fedinfo, "--federates=1")
h.helicsFederateInfoSetTimeProperty(fedinfo, h.HELICS_PROPERTY_TIME_DELTA, 0.01)

vfed = h.helicsCreateValueFederate("Federate1", fedinfo)

pub = h.helicsFederateRegisterGlobalTypePublication(vfed, "topic_name", "double", "")

h.helicsFederateEnterExecutingMode(vfed)

this_time = 0.0

for t in range(5, 10):

    currenttime = h.helicsFederateRequestTime(vfed, t)

    h.helicsPublicationPublishDouble(pub, pi)
    print("SENDER: Sending value pi = {} at time {} to RECEIVER".format(pi, currenttime))

    time.sleep(1)

h.helicsFederateDisconnect(vfed)
h.helicsFederateDestroy(vfed)