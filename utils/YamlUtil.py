# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
import os
import yaml
class YamlReader():

	def __init__(self,yamlf):
		'''
		判断文件是否存在
		:param yamlf:
		'''
		if os.path.exists(yamlf):
			self.yamlf = yamlf
		else:
			raise FileNotFoundError('文件不存在')
		self._data=None
		self._data_all = None

	def data(self):
		'''
		单个文档
		:return:
		'''
		if not self._data:
			with open(self.yamlf, 'r', encoding='utf-8') as f:

				self._data = yaml.safe_load(f)
			return self._data

	def data_all(self):
		'''
		多个文档，以列表形式返回
		:return:
		'''
		if not self._data_all:
			with open(self.yamlf, 'r', encoding='utf-8') as f:

				self._data_all = list(yaml.safe_load_all(f))

			return self._data_all

