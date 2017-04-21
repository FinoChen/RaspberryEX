import urllib2
import json

def get_url_data():
    url = "http://192.168.0.154:8000/TM"
    data = json.loads(urllib2.urlopen(url).read())
    return data



