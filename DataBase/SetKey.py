import time

def datatime_to_key(current_time):
    return time.strftime('%Y-%m-%d %H:%M:%S',current_time)