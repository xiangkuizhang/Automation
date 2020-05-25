# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK

from config import Conf
from utils.YamlUtil import YamlReader
from base.ExcelData import Data
from data.ExcelConfig import TestSteps,CaseData,Elements,TestCases
from base.BaseAction import Action,screenshot_allure
from base.DesiredCaps import appium_desired_caps
from utils.LogUtil import myLog
from utils.HTMLTestRunner import HTMLTestRunner
import os
import allure
'''
重构代码
pytest测试用例编写，新建测试文件

'''

log = myLog('operate')
# data = Data(Conf.testcase_path)
# run_list = data.run_list()
#执行测试用例的列表


class Operate():
	#setup class
	def __init__(self,driver):
		self.driver = driver

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

	def test_run(self,run_case):
		log.info("执行用例内容:{}".format(run_case))
		self.step(run_case)

	@screenshot_allure
	def step(self,data,run_case):
		tc_id = run_case[TestSteps.STEP_TC_ID]
		#获取步骤

		steps = data.get_steps_by_tc_id(tc_id)

		allure.dynamic.feature(run_case[TestCases.CASSE_NOTE])
		allure.dynamic.story(run_case[TestCases.CASES_DESC])
		allure.dynamic.title(run_case[CaseData.DATA_TC_ID]+"-"+run_case[CaseData.DATA_NAME])

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
				with allure.step(step[TestSteps.STEP_NAME]):
					action_method(**param_value)

			else:
				log.error("没有operate信息：{}".format(operate))




if __name__ =="__main__":

	report = Conf.repot_path+os.sep+"测试报告.html"
	with open(report,"wb+") as report:
		runner = HTMLTestRunner(stream=report,verbosity=2,title="移动端自动化测试报告",description="关键字驱动测试" )

#test cases 备注 feature
#test cases 描述 story
#case data  caseID+用例名称 title
#test steps  步骤名称   step
