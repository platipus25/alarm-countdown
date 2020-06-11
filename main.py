from datetime import datetime, timedelta

# time until clock time (ex. 2:30)
# time since clock time
# timer (will also tell you what time that is)
# clock 
# returns unix timestamp


def time_until():

    return

def timer(hours = 0, minutes = 0, seconds = 0):
    
    return time() + mktime(localtime()._replace(hour=hours, minute=minutes, seconds=seconds))

def clock():
    return parse_parse(parse(time()))

print(timer)
print(clock())
