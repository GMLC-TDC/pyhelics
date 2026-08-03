import helics as h

fedinfo = h.helicsCreateFederateInfo()
h.helicsFederateInfoSetCoreName(fedinfo, "Federate2")
h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")
h.helicsFederateInfoSetCoreInitString(fedinfo, "--federates=1")
h.helicsFederateInfoSetTimeProperty(fedinfo, h.HELICS_PROPERTY_TIME_DELTA, 0.01)

vfed = h.helicsCreateValueFederate("Federate2", fedinfo)

sub = h.helicsFederateRegisterSubscription(vfed, "topic_name", "")

h.helicsFederateEnterExecutingMode(vfed)

value = 0.0
currenttime = -1

while currenttime <= 100:

    currenttime = h.helicsFederateRequestTime(vfed, 100)

    value = h.helicsInputGetString(sub)
    print("RECEIVER: Received value = {} at time {} from SENDER".format(value, currenttime))

h.helicsFederateDisconnect(vfed)
h.helicsFederateDestroy(vfed)