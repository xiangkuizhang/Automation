# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
import xlrd
import os

class SheetTypeError:
	pass
class ExcelReader:

	def __init__(self,excel_file,sheet_by):
		#判断文件是否存在
		if os.path.exists(excel_file):
			self.excel_file = excel_file
			self.sheet_by = sheet_by
			self._data = list()
		else:
			raise FileNotFoundError("文件不存在，请确认")

	def data(self):
		if not self._data:
			workbook = xlrd.open_workbook(self.excel_file)
			if type(self.sheet_by) not in [str,int]:
				raise SheetTypeError('sheet类型不正确，请检查')
			elif isinstance(self.sheet_by,int):
				sheet = workbook.sheet_by_index(self.sheet_by)
			elif isinstance(self.sheet_by,str):
				sheet = workbook.sheet_by_name(self.sheet_by)
			#获取首行信息
			title = sheet.row_values(0)

			# data = []
			for r in range(1,sheet.nrows):
				row_value = sheet.row_values(r)
				self._data.append(dict(zip(title,row_value)))
		return self._data

if __name__ =="__main__":
	reader =ExcelReader("../data/data.xls","TestCases")
	print(reader.data())