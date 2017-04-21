import redis

class TMDatabase(object):
    
    def __init__(self):
        self.database = redis.StrictRedis()

    def set_TMvalue(self,key,value1,value2):
        self.database.hmset(key,{"temperature":value1,"hmidity":value2})

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