#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:

from .base import *
from .xml import *

class IndexHandler(BaseHandler):
    def get(self):
    	self.post()
    	# self.write("Hello World")
    	# self.finish()
    def post(self):
    	key=self.get_argument('key','')
    	x=Xml()
    	data=x.readxml()
    	if key!='':
    		data=x.searchxml(key,data)
    	self.set_header("Access-Control-Allow-Origin", "*")
    	self.set_header("Content-Type", "application/json")
    	self.write(x.getJSON(data))
    	self.finish()
class ListHandler(BaseHandler):
	def get(self):
		self.post()
	def post(self):
		code=self.get_argument('code','')
		if code=='':
			self.write("Please input code")
			self.finish()
		else:
			l=List(code)
			f=l.readlist(l.getlist())
			self.write(f.__dict__)
			self.finish()

handlers = [
        (r'/', IndexHandler),
        (r'/list',ListHandler)
        ]
