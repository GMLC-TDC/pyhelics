import os
import sys
import time
import helics as h
from pathlib import Path
import math
import threading

CURRENT_DIRECTORY = Path(os.path.dirname(os.path.abspath(__file__)))
TEST_FILE_PATH = CURRENT_DIRECTORY / "test_files" / "connector"

def test_connector_simple_tags():
    """
    Test the connector with simple tags.
    This test creates a HELICS app and a value federate, loads a configuration file,
    and checks the functionality of the connector with simple tags.

    It verifies that the connector can publish and receive values correctly.
    
    It should be functionally equivalent to the HELICS connector test in shared_library/appTests.cpp
    """
    if not h.helicsAppEnabled():
        # Skip the test if HELICS app is not enabled
        return
        
    fed_info = h.helicsCreateFederateInfo()
    h.helicsFederateInfoSetCoreType(fed_info, h.HELICS_CORE_TYPE_INPROC)
    h.helicsFederateInfoSetTimeProperty(fed_info, h.HELICS_PROPERTY_TIME_PERIOD, 1.0)
    h.helicsFederateInfoSetCoreName(fed_info, "ccoref5")
    h.helicsFederateInfoSetCoreInitString(fed_info, "-f2 --brokername=conn_broker --autobroker")

    conn1 = h.helicsCreateApp("connectorc1", "connector", None, fed_info)
    assert h.helicsAppIsActive(conn1)

    h.helicsAppLoadFile(conn1, str(TEST_FILE_PATH / "simple_tags.txt"))

    vFed = h.helicsCreateValueFederate("c1", fed_info)

    pub1 = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_DOUBLE, None)

    inp1 = h.helicsFederateRegisterGlobalInput(vFed, "inp1", h.HELICS_DATA_TYPE_DOUBLE, None)
    inp2 = h.helicsFederateRegisterGlobalInput(vFed, "inp2", h.HELICS_DATA_TYPE_DOUBLE, None)
    h.helicsFederateSetGlobal(vFed, "tag2", "true")

    thread1 = threading.Thread(target=h.helicsAppRun, args=(conn1,))
    thread1.start()

    h.helicsFederateEnterExecutingMode(vFed)

    test_value = 3452.562
    h.helicsPublicationPublishDouble(pub1, test_value)

    ret_time = h.helicsFederateRequestTime(vFed, 5.0)
    assert ret_time == 1.0

    val = h.helicsInputGetDouble(inp1)
    assert math.isnan(val)

    val = h.helicsInputGetDouble(inp2)
    assert val == test_value

    h.helicsFederateDestroy(vFed)
    thread1.join()

    h.helicsAppDestroy(conn1)
