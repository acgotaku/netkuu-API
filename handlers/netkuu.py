#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
import threading
import os
import http.client
import pdb
import codecs
import time
import json
import re
import logging
import xml.etree.ElementTree as ET
__ALL__ = ['Film', 'Xml','List', ]
site_config = {
    "title" : "安师大校园网视频下载!",
    "url" : """http://netkuu.icehoney.me""",
}
class FilmList:
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
            elif item.tag=="h":
                self.desc.append(item.text)
            elif item.tag=="s":
                self.desc.append(item.text)
            elif item.tag=="t":
                self.desc.append(item.text)
class Film:
    def __init__(self,film):
        for item in film:
            if item.tag=="name":
                self.name=item.text
            elif item.tag=="director":
                self.director=item.text
            elif item.tag=="actor":
                self.actor=item.text
            elif item.tag=="channelid":
                self.type=item.text
            elif item.tag=="region":
                self.region=item.text
            elif item.tag=="publishTime":
                self.publishTime=item.text
            elif item.tag=="adddate":
                self.adddate=item.text
            elif item.tag=="brief":
                text=re.sub("(\#+)([a-zA-Z0-9]{3,5});","",item.text)
                self.brief=text
class ServerXml:
    def __init__(self,server):
        for item in server:
            if item.tag=="name":
                self.name=item.text
            elif item.tag=="url":
                self.url=item.text
class Xml:
    def __init__(self,path,cache_file,url="movie.zzti.edu.cn",coding="gb18030"):
        self.url=url
        self.path=path
        self.cache_file=cache_file
        self.coding=coding
        self.lock=False
    def getxml(self,path):
        conn = http.client.HTTPConnection(self.url)
        conn.request("GET",path)
        response=conn.getresponse()
        xml=response.read()
        conn.close()
        return xml
    def savexml(self,xml,coding):
        data=xml.decode(encoding=coding,errors='replace')
        self.lock=True
        f=open(self.cache_file,"w")
        f.write(data)
        f.close()
        self.lock=False
    def updatexml(self):
        if os.path.exists(self.cache_file):
            mtime=os.path.getmtime(self.cache_file)
            now_time=time.time()
            if now_time-mtime<86400:
                return
        t = threading.Thread(target=self.savexml, args = (self.getxml(self.path),self.coding))
        t.daemon = True
        t.start()
    def getJSON(self,data):
        json_string="[]"
        if data is None:
            return json_string
        if type(data).__name__=="list":
            json_string = json.dumps([item.__dict__ for item in data])
        else:
            json_string = json.dumps(data.__dict__)
        return json_string
class Search(Xml):
    def __init__(self,path,cache_file,url="movie.zzti.edu.cn",coding="gb18030"):
        Xml.__init__(self,path,cache_file,url,coding)
        self.updatexml()
    def readxml(self):
        films=[]
        if os.path.exists(self.cache_file) and not self.lock:
            f = codecs.open(self.cache_file, mode='r', encoding='utf8')
        else:
            return films
        data=f.read()
        try:
            root = ET.fromstring(data)
        except:
            return None
        f.close()
        for child in root:
            film=child.getchildren()
            f= FilmList(film)
            films.append(f)
        return films

    def saerchkey(self,key,data):
        result=[]
        if key=="":
            return data
        for film in data:
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
class List(Xml):
    def __init__(self,code,url="movie.zzti.edu.cn",coding="gb18030"):
        Xml.__init__(self,"","",url,coding)
        self.code=code
        self.list_url='/mov/'+code+'/url.xml'
        self.desc_url='/mov/'+code+'/film.xml'
    def getdesc(self):
        xml=self.getxml(self.desc_url)
        data=xml.decode(encoding=self.coding,errors='replace')
        try:
            root = ET.fromstring(data)
        except:
            return None
        desc=Film(root)
        return desc
    def getlist(self):
        xml=self.getxml(self.list_url)
        data=xml.decode(encoding=self.coding,errors='replace')
        try:
            root = ET.fromstring(data)
        except:
            return None
        f=FilmList(root)
        f.__delattr__("desc")
        f.code=f.code.replace("\n","")
        codes=re.split(',',f.code)
        f.code=codes[:-1]
        # pdb.set_trace()
        return f
class Item(Xml):
    def __init__(self,code,num,url="movie.zzti.edu.cn",coding="gb18030"):
        self.code=code
        self.num=num
        self.down_url='/xy_path.asp?a='+num+'&b='+self.code
        Xml.__init__(self,"","",url,coding)
    def getdown(self):
        xml=self.getxml(self.down_url)
        data=xml.decode(encoding=self.coding,errors='replace')
        item_url=re.split(re.escape("|||"),data)
        return item_url
class ServerList(Xml):
    def __init__(self,path,cache_file,url,coding="utf8"):
        Xml.__init__(self,path,cache_file,url,coding)
        self.updatexml()
    def readlist(self):
        servers=[]
        if os.path.exists(self.cache_file) and not self.lock:
            f = codecs.open(self.cache_file, mode='r', encoding='utf8')
        else:
            return servers
        data=f.read()
        f.close()
        try:
            root = ET.fromstring(data)
        except:
            return None  
        for child in root:
            server=child.getchildren()
            s=ServerXml(server)
            servers.append(s)
        return servers
