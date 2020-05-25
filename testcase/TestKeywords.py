# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
'''
创建测试用例方法
重构代码
增加运行 setup teardown

'''
import pytest
from utils.LogUtil import myLog
from config import Conf
from base.ExcelData import Data
from testcase.operate.KeywordOperatePytest import Operate

log = myLog('TestKeyword')
data = Data(Conf.testcase_path)
run_list = data.run_list()


class TestKeyword:


	# def setup_class(self):
	# 	self.dirver =appium_desired_caps()

	# def setup(self):
	# 	self.dirver.launch_app()
	@pytest.mark.parametrize('run_case',run_list)
	def test_run(self,start_appium_desired,run_case):
		self.driver = start_appium_desired
		self.driver.launch_app()
		log.info(self.driver.launch_app())
		log.info("执行用例内容:{}".format(run_case))
		Operate(self.driver).step(data,run_case)



	def teardwon(self):
		self.dirver.close_app()


	# def teardwon_class(self):
	# 	self.dirver.quit()

if __name__=="__main__":
	A = TestKeyword()
	A.test_run()