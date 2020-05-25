# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK

from utils.LogUtil import myLog
from utils.ExcelUtil import ExcelReader
from data.ExcelConfig import ExcelSheet,TestCases,TestSteps,CaseData,Elements

'''
数据处理：获取运行测试用例列表，根据列表执行测试内容，测试步骤，action
1。初始化测试用例，分别初始化 4个sheet对象
2。分别定义读取4个sheet方法
3。获取全部真实有效的测试用例 方法
4。根据TCID获取相应的列表数据
5。判断是否运行列， y 执行测试用例
6。获取运行的测试用例列表
'''

#1。初始化测试用例，分别初始化 4个sheet对象
#创建类，初始化用例文档


class Data:
	def __init__(self,case_file):
		self.log = myLog()
		#初始化 4个sheet对象
		# self.reder_cases = ExcelReader(case_file,"TestCases")
		# self.reder_data = ExcelReader(case_file, "CaseData")
		# self.reder_steps = ExcelReader(case_file, "TestSteps")
		# self.reder_elements = ExcelReader(case_file, "Elements")
		self.reder_cases = ExcelReader(case_file, ExcelSheet.TEST_CASE)
		self.reder_data = ExcelReader(case_file, ExcelSheet.TEST_DATA)
		self.reder_steps = ExcelReader(case_file, ExcelSheet.TEST_STEP)
		self.reder_elements = ExcelReader(case_file, ExcelSheet.TEST_ELEMENT)

	#2。分别定义读取4个sheet方法

	def get_cases_sheet(self):
		'''
		获取测试用例test case sheet数据
		:return:
		'''
		return self.reder_cases.data()

	def get_data_sheet(self):
		return  self.reder_data.data()
	def get_steps_sheet(self):
		return self.reder_steps.data()
	def get_elements_sheet(self):
		return self.reder_elements.data()


#获取全部真实有效的测试用例 方法
# 获取testcase 数据
#获取测试数据 data case
#获取测试步骤 setp
#获取 element

	def get_case_all(self):
		'''
		获取全部测试用例，过滤空的内容，过滤action不为y的数据
		:return:
		'''
		data_list =self.get_cases_sheet()
		res =self.get_no_empty(data_list,TestCases.CASES_TC_ID)
		return res

	def get_data_all(self):
		data_list = self.get_data_sheet()
		res = self.get_no_empty(data_list,CaseData.DATA_TC_ID)
		return res

	def get_steps_all(self):
		data_list = self.get_steps_sheet()
		res = self.get_no_empty(data_list,TestSteps.STEP_TC_ID)
		return res

	def get_elements_all(self):
		data_list = self.get_elements_sheet()
		res = self.get_no_empty(data_list,Elements.ELEMENTS_TC_ID)
		return res
	def get_no_empty(self,data_list,condition):
		'''
		按条件获取非空数据
		:param data_list:
		:param condition:
		:return:
		'''
		res = []
		for data in data_list:
			if data[condition] != "":
				res.append(data)
		return res


#根据TCID获取相应的列表数据
#1 data
	def get_data_by_tc_id(self,tc_id):
		#获取全部数据
		data_all = self.get_data_all()
		#根据tc_id 获取数据列表
		data_all_tc = self.get_by_tc_id(data_all,tc_id)
		return data_all_tc

	def get_steps_by_tc_id(self,tc_id):
		steps_all = self.get_steps_sheet()
		steps_all_tc = self.get_by_tc_id(steps_all,tc_id)
		return steps_all_tc

	def get_element_by_tc_id(self,tc_id):
		elements_all = self.get_elements_sheet()
		elements_all_tc = self.get_by_tc_id(elements_all,tc_id)
		return elements_all_tc


	def get_elements_by_element(self,tc_id,element_name):
		'''
		根据步骤中sheet重的元素名和tc_id 来获取相应的数据
		:param element_name:
		:param tc_id:
		:return:
		'''
		elements=self.get_element_by_tc_id(tc_id)
		res =None
		for ele in elements:
			if str(ele[Elements.ELEMENTS_NAME])== str(element_name):
				res = ele
		return res

	def get_by_tc_id(self,data_list,tc_id):
		'''
		根据tc_id来获取数据，生成新的列表
		:param data_list:
		:param tc_id:
		:return:
		'''
		data_all_tc = []
		for data in data_list:
			if data[TestCases.CASES_TC_ID] == tc_id:
				data_all_tc.append(data)
		return data_all_tc

#判断是否运行列， y 执行测试用例
#test case
	def get_run_cases(self):
		run_list = self.get_case_all()
		run_case_list = []
		for line in run_list:
			if str(line[TestCases.CACES_IS_RUN]).lower()=='y':
				run_case_list.append(line)
		return run_case_list
#test data
	def get_run_data(self,tc_id):
		data_list = self.get_data_all()
		run_data_list=[]
		for data in data_list:
			if str(data[CaseData.DATA_IS_RUN]).lower() =='y' and tc_id in data[CaseData.DATA_TC_ID]:
				run_data_list.append(data)
		return run_data_list

#获取运行测试用例列表

	def run_list(self):
		'''
		获取test case 执行测试用例列表
		:return:
		'''
		cases=self.get_run_cases()
		self.log.debug("获取TestCase表测试的个数{},数据内容{}".format(len(cases),cases))

		#根据这个列表中的TC_ID来获取对应的data数据
		data_list = list()
		for case in cases:
			tc_id = case[TestCases.CASES_TC_ID]
			#备注
			desc = case[TestCases.CASES_DESC]
			#描述
			note = case[TestCases.CASSE_NOTE]
			tmp_data_list = self.get_run_data(tc_id)
			print(tmp_data_list)
			for data in tmp_data_list:
				data.update({TestCases.CASES_DESC:desc})
				data.update({TestCases.CASSE_NOTE:note})
			#data_list.append(self.get_run_data(tc_id))
			print(tmp_data_list)
			data_list.extend(tmp_data_list)
		self.log.debug("获取CaseData运行的个数{},数据内容{}".format(len(data_list),data_list))
		return data_list


if __name__ =="__main__":
	res_data=Data("../data/data.xls")
	# print(res_data.get_case_all())
	# print(res_data.get_data_all())
	# print(res_data.get_steps_all())[0]
	# print(res_data.get_elements_all())
	# print(res_data.get_data_by_tc_id("HomePage"))
	# print(res_data.get_run_cases())
	# print(res_data.get_run_data('HomePage'))
	# print(res_data.get_elements_by_element('HomePage','Baidu'))
	print(res_data.run_list()[0])