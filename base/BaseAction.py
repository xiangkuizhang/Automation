# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.LogUtil import myLog
import allure
import datetime
class  Action():
	def __init__(self,driver):
		self.driver = driver
		self.log = myLog('BasePage')

#元素定位
#by_id by_xpath ,元素等待
# click
#send_keys
#toast

	def by_xpath(self,value):
		'''
		通过xpath 元素定位
		:param value:
		:return:
		'''
		return self.by_find_element(By.XPATH,value)

	def by_id(self,value):
		'''
		通过ID元素定位
		:return:
		'''
		return self.by_find_element(By.ID, value)

	def send_keys(self,**kwargs):
		'''
		通过by输入内容
		:param value:
		:param send_value:
		:return:
		'''
		by,value = kwargs["by"],kwargs["value"]

		if by=="id":
			loc = self.by_id(value)
		elif by=="xpath":
			loc = self.by_xpath(value)
		loc.send_keys(kwargs["send"])

	def by_find_element(self,by,value,timeout=30,poll=3):
		'''
		隐式等待
		:param by:
		:param value:
		:param timeout:
		:param poll:
		:return:
		'''
		try:
			WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
			return self.driver.find_element(by, value)
		except Exception as e:
			self.log.error("没有找到该元素{}".format(e))

	def click_btn(self,**kwargs):
		#根据by类型,进行by_id,by_xpath 方法调用
		by,value = kwargs["by"],kwargs["value"]
		if by == 'id':
			loc=self.by_id(value)
		elif by =='xpath':
			loc=self.by_xpath(value)
		loc.click()

	def is_toast_exsit(self,**kwargs):
		'''

		:return:
		'''
		#1.使用by_find_element寻找元素，类型xpath,value自定义
		#2.使用webdriver wait 获取信息 text
		try:
			text = kwargs["expect"]
			toast_loc = "//*[contains(@text,'"+ text +"')]"
			ele = WebDriverWait(self.driver,timeout=3,poll_frequency=0.5).until(lambda x:x.find_element(By.XPATH,toast_loc))
			self.log("获取toast内容为:{}".format(ele.text))
			return True
		except Exception as e:
			self.log("toast获取失败,错误信息{}".format(e))
			return False

	def assert_toast_result(self,**kwargs):
		toast_result=self.is_toast_exsit(**kwargs)
		assert toast_result
		# try:
		# 	assert toast_result
		# except Exception as e:
		# 	png=self.driver.get_screenshot_as_png()
		# 	allure.attach(png,"toast错误",allure.attachment_type.PNG)
		# 	raise e

	#定义一个装饰器
def screenshot_allure(func):
	def get_screenshot(self,*args,**kwargs):
		try:
			assert func(*args,**kwargs)
		except Exception as e:
			png = self.driver.get_screenshot_as_png()
			name= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			allure.attach(png, name, allure.attachment_type.PNG)
			raise e
	return get_screenshot