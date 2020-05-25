# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
#1 定义sheet 定义
class ExcelSheet:
	TEST_CASE = "TestCases"
	TEST_DATA = "CaseData"
	TEST_STEP = "TestSteps"
	TEST_ELEMENT="Elements"

#每个sheet数据的映射

class TestCases:
	#序号	描述	TC_ID	是否运行	备注
	CASES_NUM = "序号"
	CASES_DESC = "描述"
	CASES_TC_ID="TC_ID"
	CACES_IS_RUN = "是否运行"
	CASSE_NOTE = "备注"

class TestSteps:
	#TC_ID	步骤ID	步骤名称	操作	元素名称	数据
	STEP_TC_ID="TC_ID"
	STEP_ID="步骤ID"
	STEP_NAME="步骤名称"
	STEP_OPERATE="操作"
	STEP_ELEMENT="元素名称"
	STEP_DATA="数据"

class CaseData:
	#TC_ID	CASE_ID	是否运行	用例名称	测试数据	期望结果
	DATA_TC_ID="TC_ID"
	DATA_IS_RUN = "是否运行"
	DATA_NAME="用例名称"
	DATA_INPUT="测试数据"
	DATA_EXPECT_RESULT="期望结果"

class Elements:
	#TC_ID	元素名称	定位类型	元素信息
	ELEMENTS_TC_ID="TC_ID"
	ELEMENTS_NAME="元素名称"
	ELEMENTS_BY="定位类型"
	ELEMENTS_VALUE="元素信息"
