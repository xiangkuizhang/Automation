# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
#定义命令行选项
import pytest
from base.StartAppium import *
import time
from base.DesiredCaps import appium_desired_caps


def pytest_addoption(parser):
		parser.addoption("--cmdopt",action='store',default='run',help=None)

#接受命令
@pytest.fixture(scope="session")
def cmdopt(request):
	return request.config.getoption("--cmdopt")

#调用接受到的命令
@pytest.fixture(scope="session")
def start_appium_desired(cmdopt):
	opt = eval(cmdopt)
	host = opt["host"]
	port = opt["port"]
	bpport = opt["bpport"]
	udid = opt["udid"]

	print(opt)


	if udid in str(get_devices()):
	    appium_start(host,port,bpport,udid)
	    time.sleep(5)
	    if not check_port():
	        driver = appium_desired_caps(host,port)
	return driver





