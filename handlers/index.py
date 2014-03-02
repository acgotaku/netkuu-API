#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:

from .base import *
from .xml import *
from .server import *
site_config = {
    "title" : "安师大校园网视频下载!",
    "url" : """http://netkuu.icehoney.me""",
}
class IndexHandler(BaseHandler):
    def get(self):
    	self.render("index.html", title=site_config['title'])
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
        self.render("list.html",title=site_config['title'])
        # self.post()
    def post(self):
        code=self.get_argument('code','')
        item=self.get_argument('item','False')
        if code=='':
            self.write("Please input code")
            self.finish()
        elif item=='False':
            l=List(code)
            f=l.getdesc()
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Content-Type", "application/json")
            self.write(l.getJSON(f))
            self.finish()
        else:
            l=List(code)
            f=l.readlist(l.getlist())
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Content-Type", "application/json")
            self.write(l.getJSON(f))
            self.finish()    


class ItemHandler(BaseHandler):
    def get(self):
        self.render("item.html",title=site_config['title'])
    def post(self):
        num=self.get_argument('num','')
        code=self.get_argument('code','')
        if code=='' or num=='':
            self.write("Please input code or num")
            self.finish()
        else:
            i=List(code)
            url=i.getdown(num)
            self.set_header("Access-Control-Allow-Origin", "*")
            # self.set_header("Content-Type", "application/x-gzip")
            self.write(str(url[1]))
            self.finish()
class ServerHandler(BaseHandler):
    def get(self):
        self.post()
    def post(self):
        s=ServerList()
        data=s.readlist()
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")
        self.write(s.getJSON(data))
        self.finish()
handlers = [
        (r'/', IndexHandler),
        (r'/list',ListHandler),
        (r'/item',ItemHandler),
        (r'/server',ServerHandler)
        ]
