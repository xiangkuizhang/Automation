# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
from config import Conf
from utils.YamlUtil import YamlReader

def get_keyword(name):
	#读取配置文件
	keyword_file =Conf.keywords_path
	#Yamlreader ,data()
	reader = YamlReader(keyword_file).data()
	#key 获取值 name
	value = reader[name]
	return value

class A :
	name = 'test'
	def get_name(self):
		print(self.name)

if __name__=="__main__":
	# value =get_keyword('verify_toast')
	# print(value)
	a = A()
	print(getattr(a,"get_name"))