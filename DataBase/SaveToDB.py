import time
import SetKey 
import GetUrlData
from DBoperation import TMDatabase

def save(database):
    while True:
        TMvalue = GetUrlData.get_url_data()
        key = SetKey.datatime_to_key(time.localtime(time.time()))
        database.set_TMvalue(key,str(TMvalue[0]),str(TMvalue[1]))
        database.save()