
#!/usr/bin/env python2.7
#coding=utf-8
import json
import urllib2
# based url and required header
url = "http://127.0.0.1/zabbix/api_jsonrpc.php"
header = {"Content-Type": "application/json"}
# request json
data = json.dumps(
		{
		"jsonrpc":"2.0",
		"method":"host.get",
		"params":{
		"output":["hostid","name"],
		"filter":{"host":""}
		},
		"auth":"e65e2b4428797bc22f4a6a657bdde47a", # the auth id is what auth script returns, remeber it is string
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
	print "Number Of Hosts: ", len(response['result'])
	for host in response['result']:
		print "Host ID:",host['hostid'],"Host Name:",host['name']
