#!/usr/bin/env python2.7
#coding=utf-8
import json
import urllib2
from urllib2 import URLError 
import sys,argparse

class zabbix_plugin:
  def __init__(self):
	# based url and required header
	url = "http://127.0.0.1/zabbix/api_jsonrpc.php"
	header = {"Content-Type": "application/json"}
  def login(self):
	# auth user and password
	data = json.dumps({
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                	"user": "Admin",
	                "password": "zabbix"
        		},
                "id": 0
	})

	# create request object
	request = urllib2.Request(url,data)
	for key in self.header:
        	request.add_header(key,header[key])
	# auth and get authid
	try:
        	result = urllib2.urlopen(request)
	except urllib2.URLError as e:
        	print "Auth Failed, Please Check Your Name And Password:",e.code
	else:
        	response = json.loads(result.read())
        	result.close()
	        print "Auth Successful. The Auth ID Is:",response['result']
		self.authID = response['result'] 
	        return self.authID 

  def create_hostgroup(self,hostgroup=''):
	# request json
	data = json.dumps({
		"jsonrpc":"2.0",
		"method":"hostgroup.create",
		"params":{
			"name": hostgroup
		},
		"auth":self.login(), # the auth id is what auth script returns, remeber it is string
		"id":1,
		})
	# create request object
	request = urllib2.Request(url,data)
	for key in header:
		request.add_header(key,header[key])
		# get host list
	try:
		result = urllib2.urlopen(request)
	except urllib2.URLError as e:
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
		elif hasattr(e, 'code'):
			print 'The server could not fulfill the request.'
			print 'Error code: ', e.code
	else:
		response = json.loads(result.read())
		result.close()
		print "add Hostgroup:", hostgroup, " id: ", response['result']['groupids']

if __name__ == "__main__":
 zabbix=zabbix_plugin()
 parser=argparse.ArgumentParser(description='zabbix  api ',usage='%(prog)s [options]')
 parser.add_argument('-H','--host',nargs='?',dest='listhost',default='host',help='list host')
 parser.add_argument('-G','--group',nargs='?',dest='listgroup',default='group',help='list group')
 parser.add_argument('-T','--template',nargs='?',dest='listtemp',default='template',help='list template')
 parser.add_argument('-A','--add-group',nargs=1,dest='addgroup',help='create group')
 parser.add_argument('-C','--add-host',dest='addhost',nargs=3,metavar=('192.168.2.1', 'test01,test02', 'Template01,Template02'),help='add host.')
 parser.add_argument('-d','--disable',dest='disablehost',nargs=1,metavar=('192.168.2.1'),help='disable host')
 parser.add_argument('-D','--delete',dest='deletehost',nargs='+',metavar=('192.168.2.1'),help='del host')
 parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')
 if len(sys.argv)==1:
 	print parser.print_help()
 else:
	 args=parser.parse_args()
if args.addgroup:
 zabbix.create_hostgroup(args.addgroup[0])
