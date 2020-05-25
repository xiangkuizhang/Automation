# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
import unittest
from config import Conf
from utils.YamlUtil import YamlReader
from base.ExcelData import Data
from data.ExcelConfig import TestSteps,CaseData,Elements
from base.BaseAction import Action
from base.DesiredCaps import appium_desired_caps
from utils.LogUtil import myLog
import ddt
from utils.HTMLTestRunner import HTMLTestRunner
import os
'''
多个用例参数化，ddt ,file_data ,data
data 自持元组，字典，列表 unpack
1.删除无用的代码
2.获取测试用例的列表[[{}],[{}]] 转换成[{},{}],修改ExcelData run_list
3.增加新的测试用例，调用 单条用例执行 方法不做修改
4.ddt  相关代码， ddt.ddt ddt.data 不实用unpack
5.输出测试报告
6.运行、调试


'''

log = myLog('operate')
data = Data(Conf.testcase_path)
run_list = data.run_list()
#执行测试用例的列表

@ddt.ddt
class Operate(unittest.TestCase):
	#setup class
	@classmethod
	def setUpClass(cls):
		cls.driver = appium_desired_caps()

	def setUp(self):
		self.driver.launch_app()

	def get_keyword(self,name):
		keyword_file = Conf.keywords_path
		reader = YamlReader(keyword_file).data()
		value = reader[name]
		return value

	def str_to_dict(self,content):
		res = {}
		if ',' not in str(content):
			c = content.split('=')
			res[c[0]] = c[1]
			return res
		elif ',' in str(content):
			for r in str(content).split(','):
				c = r.split('=')
				res[c[0]] = c[1]
			return res
	@ddt.data(*run_list)
	def test_run(self,run_case):
		log.info("执行用例内容:{}".format(run_case))
		self.step(run_case)


	def step(self,run_case):
		tc_id = run_case[TestSteps.STEP_TC_ID]
		#获取步骤
		steps = data.get_steps_by_tc_id(tc_id)
		for step in steps:
			log.debug("执行步骤:{}".format(step))
			elements = step[TestSteps.STEP_ELEMENT]
			element = data.get_elements_by_element(step[TestSteps.STEP_TC_ID], elements)
			log.debug("元素信息:{}".format(element))
			operate = self.get_keyword(step[TestSteps.STEP_OPERATE])
			#定义方法参数：字典
			param_value = dict()
			by = element[Elements.ELEMENTS_BY]
			value = element[Elements.ELEMENTS_VALUE]
			send_value = step[TestSteps.STEP_DATA]
			data_input = run_case[CaseData.DATA_INPUT]
			send = self.str_to_dict(data_input)
			expect = run_case[CaseData.DATA_EXPECT_RESULT]
			if send_value:
				data_input = run_case[CaseData.DATA_INPUT]
				send = self.str_to_dict(data_input)
				expect = run_case[CaseData.DATA_EXPECT_RESULT]
				param_value["by"]= by
				param_value["value"] = value
				param_value["send"] = send[send_value]
				param_value['expect']=expect
			else:

				param_value["by"] = by
				param_value["value"] = value
			if operate:
				action_method = getattr(Action(self.driver),operate)
				log.debug("该关键字是:{}".format(operate))
				print(action_method)
				action_method(**param_value)
			else:
				log.error("没有operate信息：{}".format(operate))


	def tearDown(self):
		self.driver.close_app()
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()


if __name__ =="__main__":
	suite = unittest.makeSuite(Operate)
	report = Conf.repot_path+os.sep+"测试报告.html"
	with open(report,"wb+") as report:
		runner = HTMLTestRunner(stream=report,verbosity=2,title="移动端自动化测试报告",description="关键字驱动测试" )

		runner.run(suite)
