# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import time
import helics as h
import pytest
import pytest as pt

from test_init import createBroker, createValueFederate, destroyFederate, destroyBroker, createMessageFederate

import os


def rm(filename, force=True):
    if os.path.exists(filename):
        os.remove(filename)


def isfile(filename):
    return os.path.exists(filename)


@pt.fixture
def broker():
    brk = h.helicsCreateBroker("zmq", "gbrokertest", "--root")
    yield brk
    h.helicsBrokerDisconnect(brk)
    assert h.helicsBrokerIsConnected(brk) == False
    h.helicsCloseLibrary()


def test_other_tests_broker_creation():

    argv = ["--root"]

    brk = h.helicsCreateBrokerFromArgs("zmq", "gbrokerc", argv)
    assert h.helicsBrokerGetIdentifier(brk) == "gbrokerc"

    with pt.raises(h.HelicsException):
        argv.append("--log-level=what_logs?")
        brk2 = h.helicsCreateBrokerFromArgs("zmq", "gbrokerc", argv)

    h.helicsBrokerDisconnect(brk)


def test_broker_test_make_broker_connections(broker):
    with pt.raises(h.HelicsException):
        h.helicsBrokerMakeConnections(broker, "invalidfile.json")


def test_broker_test_make_core_connections(broker):
    cr = h.helicsCreateCoreFromArgs("zmq", "gcore", ["--broker=gbrokertest"])

    assert h.helicsCoreGetIdentifier(cr) == "gcore"

    with pt.raises(h.HelicsException):
        h.helicsCoreMakeConnections(cr, "invalidfile.json")

    h.helicsCoreDisconnect(cr)


def test_federate_info_tests_set_broker_init_string():
    fi = h.helicsCreateFederateInfo()
    h.helicsFederateInfoSetBrokerInitString(fi, "")


def test_other_tests_core_creation(broker):

    cr = h.helicsCreateCoreFromArgs("zmq", "gcore", ["--broker=gbrokertest"])

    assert h.helicsCoreGetIdentifier(cr) == "gcore"

    # TODO: why is this not raising an exception?
    with pt.raises(h.HelicsException):
        cr2 = h.helicsCreateCoreFromArgs("test", "gcore2", ["--broker=gbrokerc", "--log-level=what_logs?"])

    h.helicsCoreDisconnect(cr)


def test_system_broker_global_value():
    brk = h.helicsCreateBroker("ipc", "gbrokerc", "--root")
    globalVal = "this is a string constant that functions as a global"
    globalVal2 = "this is a second string constant that functions as a global"
    h.helicsBrokerSetGlobal(brk, "testglobal", globalVal)
    q = h.helicsCreateQuery("global", "testglobal")
    res = h.helicsQueryBrokerExecute(q, brk)
    assert globalVal in str(res)
    h.helicsBrokerSetGlobal(brk, "testglobal2", globalVal2)
    # h.helicsQueryFree(q)
    q = h.helicsCreateQuery("global", "testglobal2")
    res = h.helicsQueryBrokerExecute(q, brk)
    assert globalVal2 in str(res)
    h.helicsBrokerDisconnect(brk)
    # h.helicsQueryFree(q)
    assert h.helicsBrokerIsConnected(brk) is False
    h.helicsBrokerFree(brk)


def test_system_test_core_global_value1():

    brk = h.helicsCreateBroker("zmq", "gbrokerc", "--root")
    cr = h.helicsCreateCore("zmq", "gcore", "--broker=gbrokerc")

    globalVal = "this is a string constant that functions as a global"
    _ = "this is a second string constant that functions as a global"

    h.helicsCoreSetGlobal(cr, "testglobal", globalVal)

    # q = h.helicsCreateQuery("global", "testglobal")
    # TODO: This hangs on core execute
    # res = h.helicsQueryCoreExecute(q, cr)
    # assert res == globalVal
    # h.helicsQueryFree(q)
    # @test_broken False

    h.helicsCoreDisconnect(cr)
    h.helicsBrokerDisconnect(brk)

    assert h.helicsBrokerIsConnected(brk) is False
    h.helicsCloseLibrary()


@pt.mark.skip(reason = "Segfaults on linux")
def test_system_test_core_global_value2():
    brk = h.helicsCreateBroker("zmq", "gbrokerc", "--root")

    cr = h.helicsCreateCore("zmq", "gcore", "--broker=gbrokerc")
    connected = h.helicsCoreConnect(cr)
    assert connected == True
    assert h.helicsCoreIsConnected(cr) == True
    globalVal = "this is a string constant that functions as a global"
    globalVal2 = "this is a second string constant that functions as a global"
    h.helicsCoreSetGlobal(cr, "testglobal", globalVal)
    q = h.helicsCreateQuery("global", "testglobal")
    res = h.helicsQueryCoreExecute(q, cr)
    assert globalVal in str(res)
    h.helicsCoreSetGlobal(cr, "testglobal2", globalVal2)
    # h.helicsQueryFree(q)
    q = h.helicsCreateQuery("global", "testglobal2")
    res = h.helicsQueryCoreExecute(q, cr)
    assert globalVal2 in str(res)
    h.helicsBrokerDisconnect(brk)
    h.helicsCoreDisconnect(cr)

    # h.helicsQueryFree(q)
    assert h.helicsBrokerIsConnected(brk) == False


def test_system_test_broker_global_value():

    brk = h.helicsCreateBroker("inproc", "gbroker", "--root")
    globalVal = "this is a string constant that functions as a global"
    globalVal2 = "this is a second string constant that functions as a global"
    h.helicsBrokerSetGlobal(brk, "testglobal", globalVal)
    q = h.helicsCreateQuery("global", "testglobal")
    res = h.helicsQueryBrokerExecute(q, brk)
    assert globalVal in str(res)

    h.helicsBrokerSetGlobal(brk, "testglobal2", globalVal2)
    # h.helicsQueryFree(q)

    q = h.helicsCreateQuery("global", "testglobal2")
    res = h.helicsQueryBrokerExecute(q, brk)
    assert globalVal2 in str(res)

    h.helicsBrokerDisconnect(brk)
    # h.helicsQueryFree(q)
    assert h.helicsBrokerIsConnected(brk) is False


def test_system_test_federate_global_value():

    brk = h.helicsCreateBroker("inproc", "gbrokerc", "--root")
    cr = h.helicsCreateCore("inproc", "gcore", "--broker=gbrokerc")

    argv = ["", "--corename=gcore"]

    fi = h.helicsCreateFederateInfo()
    h.helicsFederateInfoLoadFromArgs(fi, argv)

    fed = h.helicsCreateValueFederate("fed0", fi)

    fi2 = h.helicsFederateInfoClone(fi)

    # h.helicsFederateInfoFree(fi2)
    # h.helicsFederateInfoFree(fi)

    globalVal = "this is a string constant that functions as a global"
    globalVal2 = "this is a second string constant that functions as a global"
    h.helicsFederateSetGlobal(fed, "testglobal", globalVal)
    q = h.helicsCreateQuery("global", "testglobal")
    res = h.helicsQueryExecute(q, fed)
    assert globalVal in str(res)
    h.helicsFederateSetGlobal(fed, "testglobal2", globalVal2)
    # h.helicsQueryFree(q)
    q = h.helicsCreateQuery("global", "testglobal2")
    h.helicsQueryExecuteAsync(q, fed)
    while h.helicsQueryIsCompleted(q) is False:
        time.sleep(0.20)
    res = h.helicsQueryExecuteComplete(q)
    assert globalVal2 in str(res)

    q2 = h.helicsCreateQuery("", "isinit")
    h.helicsQueryExecuteAsync(q2, fed)
    while h.helicsQueryIsCompleted(q2) is False:
        time.sleep(0.20)
    res = h.helicsQueryExecuteComplete(q2)
    assert str(res).lower() == "false"

    h.helicsFederateDisconnect(fed)

    h.helicsCoreDisconnect(cr)
    h.helicsBrokerDisconnect(brk)

    # h.helicsQueryFree(q)
    # h.helicsQueryFree(q2)
    assert h.helicsBrokerIsConnected(brk) is False

    h.helicsBrokerDisconnect(brk)
    h.helicsCoreDisconnect(cr)

    assert h.helicsBrokerIsConnected(brk) is False
    h.helicsCloseLibrary()


def test_system_tests_core_logging():
    lfile = "log.txt"
    rm(lfile, force=True)
    core = h.helicsCreateCore("inproc", "clog", "--autobroker --log_level=trace")
    h.helicsCoreSetLogFile(core, lfile)
    h.helicsCoreDisconnect(core)
    h.helicsCloseLibrary()
    assert isfile(lfile)
    rm(lfile, force=True)


def test_system_tests_broker_logging():
    lfile = "log.txt"
    rm(lfile, force=True)
    broker = h.helicsCreateBroker("inproc", "blog", "--log_level=trace")
    h.helicsBrokerSetLogFile(broker, lfile)
    h.helicsBrokerDisconnect(broker)
    h.helicsCloseLibrary()
    assert isfile(lfile)
    rm(lfile, force=True)


def test_system_tests_federate_logging():

    lfile = "log.txt"
    rm(lfile, force=True)
    core = h.helicsCreateCore("inproc", "clogf", "--autobroker --log_level=trace")

    fi = h.helicsCreateFederateInfo()
    h.helicsFederateInfoSetBrokerKey(fi, "key")
    h.helicsFederateInfoSetCoreName(fi, "clogf")
    fed = h.helicsCreateValueFederate("f1", fi)
    h.helicsFederateSetLogFile(fed, lfile)
    h.helicsFederateLogLevelMessage(fed, h.HELICS_LOG_LEVEL_TRACE, "hello")
    h.helicsFederateLogErrorMessage(fed, "hello")
    h.helicsFederateLogDebugMessage(fed, "hello")
    h.helicsFederateLogWarningMessage(fed, "hello")
    h.helicsFederateClearMessages(fed)
    h.helicsCoreSetLogFile(core, lfile)
    h.helicsCoreDisconnect(core)
    h.helicsFederateDisconnect(fed)
    # h.helicsFederateInfoFree(fi)
    h.helicsCloseLibrary()

    assert isfile(lfile)
    rm(lfile, force=True)


def test_federate_tests_federateGeneratedLocalError():

    brk = h.helicsCreateBroker("inproc", "gbrokerc", "--root")
    cr = h.helicsCreateCore("inproc", "gcore", "--broker=gbrokerc")

    argv = ["", "--corename=gcore"]

    fi = h.helicsCreateFederateInfo()
    h.helicsFederateInfoLoadFromArgs(fi, argv)

    fed1 = h.helicsCreateValueFederate("fed0", fi)

    # h.helicsFederateInfoFree(fi)
    h.helicsFederateEnterExecutingMode(fed1)

    h.helicsFederateRequestTime(fed1, 2.0)
    h.helicsFederateLocalError(fed1, 9827, "user generated local error")

    with pt.raises(h.HelicsException):
        h.helicsFederateRequestTime(fed1, 3.0)

    h.helicsFederateDestroy(fed1)
    h.helicsCoreDisconnect(cr)
    h.helicsBrokerDisconnect(brk)
    h.helicsCloseLibrary()


def test_federate_tests_federateGeneratedGlobalError():

    brk = h.helicsCreateBroker("inproc", "gbrokerc", "--root")
    cr = h.helicsCreateCore("inproc", "gcore", "--broker=gbrokerc")

    argv = ["", "--corename=gcore"]

    fi = h.helicsCreateFederateInfo()
    h.helicsFederateInfoLoadFromArgs(fi, argv)

    fed1 = h.helicsCreateValueFederate("fed0", fi)

    # h.helicsFederateInfoFree(fi)
    h.helicsFederateEnterExecutingMode(fed1)

    h.helicsFederateRequestTime(fed1, 2.0)
    h.helicsFederateGlobalError(fed1, 9827, "user generated global error")

    with pt.raises(h.HelicsException):
        h.helicsFederateRequestTime(fed1, 3.0)

    h.helicsFederateDestroy(fed1)
    h.helicsCoreDisconnect(cr)
    h.helicsBrokerDisconnect(brk)
    h.helicsCloseLibrary()
