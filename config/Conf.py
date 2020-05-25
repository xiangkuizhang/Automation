# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK

import os

#获取目录
current = os.path.dirname(os.path.dirname(__file__))
#conf 目录
conf_path = current+os.sep + 'config'
#caps.yml路径
conf_caps = conf_path + os.sep + 'caps.yml'
#log目录
log_path = current+os.sep+'logs'

#keyword 目录
keywords_path = conf_path+os.sep+"keywords.yml"

#data 路径
data_path = current+os.sep+"data"

#testcasefile 路径
testcase_path =data_path+os.sep+"data.xls"

#repot 目录
report_path = current+os.sep+ "report"

# print(conf_caps)
# print(log_path)
# print(conf_path)