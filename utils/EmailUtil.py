# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Send_email:
	def __init__(self,smtp_addr,username,password,revc,title,content=None,file=None):
		self.smtp_addr = smtp_addr
		self.username = username
		self.password = password
		self.revc = revc
		self.title=title
		self.content = content
		self.file = file

	def send_mail(self):
		message = MIMEText()
