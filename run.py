# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
import pytest
import time
import os
from base.AllureReport import allure_generate
from config.Conf import *

rp_path = report_path+os.sep+'result'
html_path = report_path+os.sep+"html"

if __name__ == '__main__':

    # cmdopt = { "host":"127.0.0.1",
    #             "port":"4723",
    #             "bpport":"4724",
    #             "udid":"emulator-5554" }
    #
    # pytest.main([f"--cmdopt={cmdopt}"])
    # # time.sleep(3)
    pytest.main()
    allure_generate(rp_path,html_path)