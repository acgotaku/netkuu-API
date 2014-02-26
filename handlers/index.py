#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:

from .base import *
from .xml import *
site_config = {
    "title" : "安师大校园网视频下载!",
    "url" : """http://netkuu.icehoney.me""",
}
class IndexHandler(BaseHandler):
    def get(self):
    	# self.post()
    	self.render("index.html", title=site_config['title'])
    	self.finish()
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
class ItemHandler(BaseHandler):
    def get(self):
        self.post()
    def post(self):
        num=self.get_argument('num','')
        code=self.get_argument('code','')
        if code=='' or num=='':
            self.write("Please input code or num")
            self.finish()
        else:
            i=List(code)
            url=i.getdown(num)
            self.write(str(url))
            self.finish()

handlers = [
        (r'/', IndexHandler),
        (r'/list',ListHandler),
        (r'/item',ItemHandler)
        ]
