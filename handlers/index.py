#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:

from .base import *

class IndexHandler(BaseHandler):
    def get(self):
        self.write("hello world!")
        self.finish()

handlers = [
        ('/', IndexHandler),
        ]
