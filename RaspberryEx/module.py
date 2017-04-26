# -*- coding:utf-8 -*-
import os.path
import tornado.web
import json

#import TMSensorData
import DataBase

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('index.html')

class test(tornado.web.RequestHandler):
    def get(self):
        self.write("hello test")

class TMHandler(tornado.web.RequestHandler):
    '''temperature and moistrue'''
    def get(self):
	import TMSensorData
        TMvalue = TMSensorData.TMData().TMvalue()
        json_TMvalue = json.dumps(TMvalue)
        #self.write("当前温度:" + str(TMvalue[0]) + "\n\r" + "当前湿度:" + str(TMvalue[1]))
        self.write(json_TMvalue)

class DBHandler(tornado.web.RequestHandler):
    def get(self):
        database = DataBase.DataBase()
        self.write(DataBase.useDataBase().use(database))
       # self.write("test ok")
        
