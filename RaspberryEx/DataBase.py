import redis
import urllib2
import json
import time

class DataBase(object):
    def __init__(self):
        self.database = redis.StrictRedis()
    
    def set_value(self,key,field,value):
        self.database.hmset(key,{field:value})

    def set_values(self,key,filed1,value1,filed2,value2):
        self.database.hmset(key,{filed1:value1,filed2:value2})

    def get_data(self,key,field):
        return self.database.hget(key,field)
    
    def get_all_data(self,key):
        return self.database.hgetall(key)

    def get_dbsize(self):
        return self.database.dbsize()

    def del_all_data(self):
        self.database.flushdb()

    def save(self):
        self.database.save()

class useDataBase(object):
    def get_url_data(self,url):
        #url = "http://192.168.0.154:8000/TM"
        data = json.loads(urllib2.urlopen(url).read())
        return data
    
    def datatime_to_key(self,current_time):
        return time.strftime('%Y-%m-%d %H:%M:%S',current_time)

    def use(self,database):
        while True:
            value = get_url_data("http://192.168.0.154:8000/TM")
            key = datatime_to_key(time.localtime(time.time()))
            database.set_values(key,str(TMvalue[0]),str(TMvalue[1]))
            database.save()