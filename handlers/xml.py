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
__ALL__ = ['Film', 'Xml', ]
url=r"movie.zzti.edu.cn";
class Film:
    def __init__(self, film):
        self.name=None
        self.code=None
        self.desc=[]
        for item in film:
            if item.tag=="a":
                self.name=item.text
            elif item.tag=="b":
                self.code=item.text
            elif item.tag=="c":
                self.desc.append(item.text)
            elif item.tag=="d":
                self.desc.append(item.text)
            elif item.tag=="e":
                self.desc.append(item.text)
            elif item.tag=="f":
                self.desc.append(item.text)
            elif item.tag=="g":
                self.desc.append(item.text)
            elif item.tag=="s":
                self.desc.append(item.text)

class Xml:
	def __init__(self):
		self.cache_file=os.getcwd() + os.sep + 'static'+os.sep+'cache'+os.sep+"Total.xml"
		self.path="/mov/xml/Total.xml";
		self.updatexml()

	def getxml(self,path):
		conn = http.client.HTTPConnection(url)
		conn.request("GET",path)
		response=conn.getresponse()
		xml=response.read()
		conn.close()
		return xml

	def savexml(self,xml):
		data=xml.decode(encoding='gb18030',errors='replace')
		f=open(self.cache_file,"w")
		f.write(data);
		f.close()

	def updatexml(self):
		# pdb.set_trace()
		if os.path.exists(self.cache_file):
			mtime=os.path.getmtime(self.cache_file)
			now_time=time.time()
			if now_time-mtime>86400:
				self.savexml(self.getxml())
		else:
			self.savexml(self.getxml())
	def readxml(self):
		films=[]
		f = codecs.open(self.cache_file, mode='r', encoding='utf8')
		data=f.read()
		root = ET.fromstring(data)
		f.close()
		for child in root:
		    film=child.getchildren()
		    f= Film(film)
		    films.append(f)
		return films
	def getJSON(self,films):
		json_string = json.dumps([item.__dict__ for item in films])
		return json_string
	def searchxml(self,key,films):
		result=[]
		for film in films:
		    if film.name.find(key)!=-1:
		        result.append(film)
		        continue
		    elif film.code.find(key)!=-1:
		        result.append(film)
		        continue
		    for item in film.desc:
		       if item:
		         if item.find(key)!=-1:
		            result.append(film)
		            break
		return result
class List:
	def __init__(self,code):
		self.code=code
		self.list_url='/mov/'+code+'/url.xml'
	def getlist(self):
		xml=Xml.getxml(self,self.list_url)
		return xml
	def readlist(self,xml):
		data=xml.decode(encoding='gb18030',errors='replace')
		root = ET.fromstring(data)
		f=Film(root)
		# f.code=f.code.replace("\n","")
		codes=re.findall("^[a-zA-Z0-9].*[a-zA-Z0-9]",f.code,re.MULTILINE)
		# pdb.set_trace()
		f.code=codes
		return f

