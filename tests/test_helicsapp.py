# -*- coding: utf-8 -*-
import helics as h
from os.path import join, dirname


def test_app_enabled():
    assert h.helicsAppEnabled()


def test_create_app_fed_info():
    # Start broker
    _ = h.helicsCreateBroker("zmq", "broker", "--federates 1")
    fed_info = h.helicsCreateFederateInfo()
    # h.helicsFederateInfoSetCoreTypeFromString(fed_info, "zmq")
    app = h.helicsCreateApp("test", "tracer", fed_info=fed_info)
    assert app is not None
    h.helicsAppDestroy(app)


def test_create_app_config_file():
    # Start broker
    _ = h.helicsCreateBroker("zmq", "broker", "--federates 2")
    fedInfo = h.helicsCreateFederateInfo()
    vfed = h.helicsCreateValueFederate("block1", fedInfo)
    sub1 = vfed.register_subscription("player1/pub1")
    sub2 = vfed.register_subscription("player1/pub2")

    app = h.helicsCreateApp(
        "player1",
        "tracer",
        join(dirname(__file__), "test_files", "helicsapp_test_example6.json"),
        fed_info=h.helicsCreateFederateInfo(),
    )
    vfed.enter_executing_mode_async()
    app.run()
    vfed.enter_executing_mode_complete()

    ret_time = vfed.request_time(5)
    assert ret_time == 1.0
    assert sub1.double == 0.5
    assert sub2.double == 0.4

    ret_time = vfed.request_time(5)
    assert ret_time == 2.0
    assert sub1.double == 0.7
    assert sub2.double == 0.6

    ret_time = vfed.request_time(5)
    assert ret_time == 3.0
    assert sub1.double == 0.8
    assert sub2.double == 0.9

    ret_time = vfed.request_time(5)
    assert ret_time == 5.0
    vfed.disconnect()

    h.helicsAppDestroy(app)
