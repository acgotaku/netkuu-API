#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
import os
import re
from .base import *
from .netkuu import *
site_config = {
    "title" : "校园网视频下载!",
    "url" : """http://netkuu.icehoney.me""",
}
class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html", title=site_config['title'])
    def post(self):
        server=self.get_cookie("server","movie.zzti.edu.cn")
        server=re.findall(r"http://(.*)/",tornado.escape.url_unescape(server))
        key=self.get_argument('key','')
        cache_file=os.getcwd() + os.sep + 'static'+os.sep+'cache'+os.sep+"Total.xml"
        s=Search("/mov/xml/Total.xml",cache_file,server[0])
        data=s.readxml();
        if key!='':
            data=s.saerchkey(key,data)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")
        self.write(s.getJSON(data))
        self.finish()
class ListHandler(BaseHandler):
    def get(self):
        self.render("list.html",title=site_config['title'])
    def post(self):
        server=self.get_cookie("server","movie.zzti.edu.cn")
        server=re.findall(r"http://(.*)/",tornado.escape.url_unescape(server))
        code=self.get_argument('code','')
        item=self.get_argument('item','False')
        if code=='':
            self.write("Please input code")
            self.finish()
        elif item=='False':
            l=List(code,server[0])
            data=l.getdesc()
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Content-Type", "application/json")
            self.write(l.getJSON(data))
            self.finish()
        else:
            l=List(code,server[0])
            data=l.getlist()
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Content-Type", "application/json")
            self.write(l.getJSON(data))
            self.finish()    


class ItemHandler(BaseHandler):
    def get(self):
        self.render("item.html",title=site_config['title'])
    def post(self):
        server=self.get_cookie("server","movie.zzti.edu.cn")
        server=re.findall(r"http://(.*)/",tornado.escape.url_unescape(server))
        num=self.get_argument('num','')
        code=self.get_argument('code','')
        if code=='' or num=='':
            self.write("Please input code or num")
            self.finish()
        else:
            i=Item(code,num,server[0])
            url=i.getdown()
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Content-Type", "application/text")
            self.write(str(url[1]))
            self.finish()
class ServerHandler(BaseHandler):
    def get(self):
        self.post()
    def post(self):
        path="/server_list.ahnu"
        url=r"www.icehoney.me"
        cache_file=os.getcwd() + os.sep + 'static'+os.sep+'cache'+os.sep+"ServerList.xml"
        s=ServerList(path,cache_file,url,"utf8")
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
