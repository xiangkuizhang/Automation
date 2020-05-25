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
import time
#单个用例编写运行调试 ，4个sheet编写，并执行一条用例，是否运行Y
#编写unittest 测试用例
#创建类 继承unit test

#测试用例实现，根据步骤，具体操作 去映射关键字方法，执行操作
#多个用例编写，参数化运 行

#根据传入操作名称，自动去BaseAction中寻找对应方法执行
#1。Excel 操作步骤与关键字的一个映射
	#创建Yaml文件
	#Excel与方法映射
	#读取配置文件，根据Key获取关键字方法

#2。根据关键字方法去BaseAction类中寻找方法，getattr内置函数
	#getattr(Action(self.drvier),操作方法)
	#根据excel操作步骤映射获取字符串格式方法名
	#判断方法是否存在，存在执行，否则不执行
	#根据字符串方法名称，getattr去获对应的函数对象
#3。方法执行，参数重构
#4。调试运行
log = myLog('operate')
class Operate(unittest.TestCase):
	#setup class

	@classmethod
	def setUpClass(cls):
		cls.driver = appium_desired_caps()
	def setUp(self):
		self.driver.launch_app()
	def get_keyword(self,name):
		# 读取配置文件
		keyword_file = Conf.keywords_path
		# Yamlreader ,data()
		reader = YamlReader(keyword_file).data()
		# key 获取值 name
		value = reader[name]
		return value
	def str_to_dict(self,content):
		# 把字符串转换成字典
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
	def test_step_new(self):
		data = Data("../data/data.xls")
		run_list = data.run_list()
		run_case = run_list[0]
		print(run_case)
		tc_id = run_case[TestSteps.STEP_TC_ID]
		steps = data.get_steps_by_tc_id(tc_id)
		for step in steps:
			log.debug("执行步骤:{}".format(step))
			#获取元素信息
			elements = step[TestSteps.STEP_ELEMENT]
			element = data.get_elements_by_element(step[TestSteps.STEP_TC_ID], elements)
			log.debug("元素信息:{}".format(element))
			#操作步骤
			operate = self.get_keyword(step[TestSteps.STEP_OPERATE])
			#定义方法参数：字典
			param_value = dict()
			by = element[Elements.ELEMENTS_BY]
			value = element[Elements.ELEMENTS_VALUE]
			send_value = step[TestSteps.STEP_DATA]

			if send_value:
				data_input = run_case[CaseData.DATA_INPUT]
				send = self.str_to_dict(data_input)
				#expect = run_case[CaseData.DATA_EXPECT_RESULT]
				param_value["by"]= by
				param_value["value"] = value
				param_value["send"] = send[send_value]
				#param_value['expect']=expect
			else:
				param_value["by"] = by
				param_value["value"] = value
			#操作是否存在，不存在不执行
			if operate:
				#根据getattr判断执行那个方法
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

