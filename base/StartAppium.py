# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
import socket
import subprocess
from utils.LogUtil import myLog
import platform
import re
log = myLog("start_Appium")
#检查端口号
def check_port(host="127.0.0.1",port ='4723'):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.connect((host,int(port)))
		s.shutdown(2)
		log.info("port %s is used"%port)
		return False
	except:
		log.info("prot %s is not used"%port)
		return True
#启动Appium
def appium_start(host="127.0.0.1",port ='4723',bpport="4724",udid=None):
	#判断端口是否存在
	if check_port(host,port):
		print("成功测试")	#定义启动参数
	cmd = "appium -a %s -p %s -bp %s -U %s --session-override"%(host,port,bpport,udid)
	#使用subprocess.call Popen
	appium_process=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

	#根据信息验证是否启动成功
	while True:
		line =str(appium_process.stdout.readline().strip(),"utf-8")
		print(line)
		if 'ussge' in line or "Error" in line:
			log.error("启动失败，错误信息：%s"%str(appium_process.stderr.readline().strip(),"utf-8"))
		if  "listener started" in line:
			log.info("启动成功，启动参数：host为%s,port为%s,bpport为%s,udid为%s"%(host,port,bpport,udid))
			break

#停止
def stop_server(port='4723'):
	if not check_port():

		#判断系统环境，是window还是Linux
		log.info(platform.system())
		system_platfor = platform.system()
		#根据系统环境，执行对应的命令
		if system_platfor.lower()=="windows":
			cmd="taskkill /f /im node.exe"
		else:
			cmd_lsof="lsof -i:{0}|grep {0}".format(port)
			cmd=cmd_lsof +"|awk '{print $2}'|xargs kill -9"
		subprocess.call(cmd,shell=True)
	else:
		log.info("该端口未运行")


#获取devices信息
def get_devices():
	cmd ="adb devices -l"
	devices_info=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	#print(devices_info.stdout.readlines())
	devices_list= []
	for line in devices_info.stdout.readlines():
		if "model" in str(line,encoding='utf-8'):
			devices_list.append(line)

	get_devices_list=[]
	for info in devices_list:
		info =str(info)
		udid = re.search(r"(.*?)device",info).group(1).strip()
		get_devices_list.append(udid)
	log.info("获取的udid:%s,"%get_devices_list)
	return get_devices_list
if __name__ == "__main__":
	check_port()
	appium_start()
	# stop_server()
	#stop_server()
	#get_devices()