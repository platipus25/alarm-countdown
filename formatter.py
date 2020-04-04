import math
import datetime
# ideas for formatter

FLOATING_POINT_SECONDS = True;

def gen(hours = 0, minutes = 0, seconds = 0, ms = 0):
    return (hours   * 60**2
          + minutes * 60**1
          + seconds * 60**0
          + ms      * 60**0 * 0.001) * 1000

sec = int(gen(5, 2, 1, 500))

def parse(ms):
    seconds = ms / 1000

    if FLOATING_POINT_SECONDS:
        seconds = round(seconds)

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

def time_until(hours = 0, minutes = 0, seconds = 0, ms = 0):
    return parse(gen_date_smart(hours, minutes, seconds, ms) - NOW)

def time_until_string(stringIn):
    return time_until(*[float(i) for i in stringIn.split(":")])

def parse_date(ms):
    return datetime.datetime.fromtimestamp(ms * 0.001)

def parse_parse(tuple):
    return datetime.timedelta(hours=tuple[0], minutes=tuple[1], seconds=tuple[2])

print(sec)
print(*parse(sec), sep=":")

print(parse_parse(parse(gen(0, 0, 1))))
print(parse_date(gen_date(10, 2, 3)))
print(parse_date(gen_date_smart(0, 2, 3)))


print(parse_parse(time_until(4, 30)))
print(parse_parse(time_until_string("7:30")))

while True:
    NOW = datetime.datetime.now().timestamp() * 1000
    TODAY_MIDNIGHT = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp() * 1000
    print(parse_parse(time_until_string("7:30")))