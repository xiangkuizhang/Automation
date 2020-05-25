# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK

from utils.YamlUtil import YamlReader
from config import Conf
from appium import webdriver
reader =YamlReader(Conf.conf_caps)
data = reader.data()



def appium_desired_caps(host,port):

	desired_caps = dict()
	desired_caps['platformName'] =data['platformName']
	desired_caps['platformVersion'] =data['platformVersion']
	desired_caps['deviceName'] =data['deviceName']
	desired_caps['appPackage']=data['appPackage']
	desired_caps['appActivity']=data['appActivity']
	desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
	desired_caps['resetKeyboard'] = data['resetKeyboard']

	driver = webdriver.Remote('http://%s:%s/wd/hub'%(host,port),desired_caps)

	driver.implicitly_wait(10)

	return driver
