import math
import datetime
# ideas for formatter

def gen(hours = 0, minutes = 0, seconds = 0, ms = 0):
    return (hours   * 60**2
          + minutes * 60**1
          + seconds * 60**0
          + ms      * 60**0 * 0.001) * 1000

sec = int(gen(5, 2, 1, 500))

def parse(ms):
    seconds = ms // 1000

    secondsOut = seconds % 60 # seconds left over after taking out minutes

    minutes = seconds // 60

    minutesOut = minutes % 60 # minutes left over after taking out seconds

    hoursOut = minutes // 60

    return (hoursOut, minutesOut, secondsOut)

NOW = datetime.datetime.now().timestamp() * 1000
TODAY_MIDNIGHT = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp() * 1000

def gen_date(hours = 0, minutes = 0, seconds = 0, ms = 0, reference_midnight = TODAY_MIDNIGHT):
    return reference_midnight + gen(hours, minutes, seconds)

def gen_date_smart(hours = 0, minutes = 0, seconds = 0, ms = 0):
    out = gen_date(hours, minutes, seconds, ms)
    if out < NOW:
        out = gen_date(hours, minutes, seconds, ms, reference_midnight = gen_date(24))
    return out

def parse_date(ms):
    return datetime.datetime.fromtimestamp(ms * 0.001)

print(sec)
print(*parse(sec), sep=":")

print(datetime.timedelta(milliseconds = gen(0, 0, 1)))
print(parse_date(gen_date(10, 2, 3)))
print(parse_date(gen_date(10, 2, 3)))