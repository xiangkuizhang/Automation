# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
from utils.LogUtil import myLog
import subprocess
#1. allure cmd 命令
log = myLog()
def allure_generate(report_path,report_html):
	allure_cmd = "allure generate %s -o %s --clean"%(report_path,report_html)
	log.info("报告地址:%s",report_path)
#2.subprocess call
	try:
		subprocess.call(allure_cmd,shell=True)
		log.info("报告地址：%s",report_html)
	except Exception as e:
		log.error("生成测试报告失败，请检查配置")
		raise e