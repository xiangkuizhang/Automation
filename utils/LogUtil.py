# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
import logging
from config import Conf
import datetime
import os

#定义日志级别的映射
log_l = {
	"info":logging.INFO,
	"debug":logging.DEBUG,
	"warnning":logging.WARNING,
	"error":logging.ERROR
}
class Logger:

	def __init__(self,log_file,log_name,log_level):
		self.log_file = log_file
		self.log_name = log_name
		self.log_level = log_level

		self.logger = logging.getLogger(log_name)
		self.logger.setLevel(log_l[log_level])

		if not self.logger.handlers:
			fh_stream = logging.StreamHandler()
			fh_stream.setLevel(log_l[log_level])
			formater = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s')
			fh_stream.setFormatter(formater)
			self.logger.addHandler(fh_stream)

			fh_file = logging.FileHandler(log_file)
			fh_file.setLevel(log_l[log_level])
			fh_file.setFormatter(formater)
			self.logger.addHandler(fh_file)


#外部调用方法
#1.初始化参数
#日志文件名称=logs+文件名
log_path = Conf.log_path
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
#扩展名
log_extension = '.log'
logfile =  os.path.join(log_path,current_date+log_extension)

loglevel = 'debug'

#2。对外方法。初始log工具类 ，提供其他类使用

def myLog(logname=__file__):
	return Logger(logfile,logname,loglevel).logger



if __name__ == '__main__':
	log = myLog('测试')
	log.info('APPinfo')