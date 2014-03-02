#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
import os
import http.client
import pdb
import codecs
import time
import json
import re
import xml.etree.ElementTree as ET
__ALL__ = ['ServerList', ]
url=r"www.icehoney.me";
class ServerXml:
	def __init__(self,server):
		for item in server:
			if item.tag=="name":
				self.name=item.text
			elif item.tag=="url":
				self.url=item.text

class ServerList:
	def __init__(self):
		self.path="/server_list.ahnu"
		self.cache_file=os.getcwd() + os.sep + 'static'+os.sep+'cache'+os.sep+"ServerList.xml"
		self.updatelist()
	def getseverlist(self,path):
		conn = http.client.HTTPConnection(url)
		conn.request("GET",path)
		response=conn.getresponse()
		xml=response.read()
		conn.close()
		return xml
	def savexml(self,xml):
		data=xml.decode(encoding='utf8',errors='replace')
		f=open(self.cache_file,"w")
		f.write(data);
		f.close()
	def updatelist(self):
		# pdb.set_trace()
		if os.path.exists(self.cache_file):
			mtime=os.path.getmtime(self.cache_file)
			now_time=time.time()
			if now_time-mtime>86400:
				self.savexml(self.getseverlist(self.path))
		else:
			self.savexml(self.getseverlist(self.path))
	def readlist(self):
		f = codecs.open(self.cache_file, mode='r', encoding='utf8')
		data=f.read()
		f.close()
		root = ET.fromstring(data)
		servers=[]
		for child in root:
			server=child.getchildren()
			s=ServerXml(server)
			servers.append(s)
		return servers
	def getJSON(self,data):
		json_string = json.dumps([item.__dict__ for item in data])
		return json_string


