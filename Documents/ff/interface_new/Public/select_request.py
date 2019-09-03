# -*- coding: utf-8 -*-
import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# from Public.request import Rquest_Api

from Public.request import Rquest_Api
class TestApi(object):
	"""
	测试用例中写入请求方式，在此进行分离
	"""
	def __init__(self,url2,key,param,way):
		self.url2 = url2
		self.key = key
		self.param = param
		self.way = way

	def selectway(self):
		if self.way == "GET":
			self.parem = {'key': self.key, 'info': self.param}
			self.response = Rquest_Api(self.url2).get(self.param, self.key)
		elif self.way == 'POST':
			#self.param = {'key': self.key, 'info': self.param}
			self.response = Rquest_Api(self.url2).post( self.param, self.key)
		elif self.way == "PUT":
			#self.param = {'key': self.key, 'info': self.param}
			self.response = Rquest_Api(self.url2).put( self.param, self.key)
		elif self.way == "DELETE":
			self.param = {'key': self.key, 'info': self.param}
			self.response = Rquest_Api(self.url2).delete( self.param, self.key)
		return self.response

# url2 = "shopappserver.showjoy.com.cn/api/shop/balancePay/getPayCode?orderNumber=6155739082804291"
# key = "appserver接口"
# param = ""
# way = "GET"
# TestApi(url2=url2,key=key,param=param,way=way).selectway()