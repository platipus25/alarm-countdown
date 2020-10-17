# ideas for formatter

def now():
    return datetime.now().timestamp()

def today_midnight():
    return datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()

def mktime(hours = 0, minutes = 0, seconds = 0):
    return (hours   * 60**2
          + minutes * 60**1
          + seconds * 60**0)

def time(seconds):
    secondsOut = seconds % 60 # seconds left over after taking out minutes

    minutes = seconds // 60

    minutesOut = minutes % 60 # minutes left over after taking out seconds

    hoursOut = minutes // 60

    return (hoursOut, minutesOut, secondsOut)

def gen_date(hours = 0, minutes = 0, seconds = 0, reference_midnight = None):
    reference_midnight = reference_midnight or today_midnight()
    return reference_midnight + mktime(hours, minutes, seconds)

def gen_date_smart(hours = 0, minutes = 0, seconds = 0):
    out = gen_date(hours, minutes, seconds)
    if out < now():
        out = gen_date(hours, minutes, seconds, reference_midnight = gen_date(24))
    return out

def time_until(hours = 0, minutes = 0, seconds = 0):
    return time(gen_date_smart(hours, minutes, seconds) - now())

def time_until_string(stringIn):
    return time_until(*[float(i) for i in stringIn.split(":")])



if __name__ == "__main__":

  from datetime import datetime, timedelta
  def parse_date(ms):
    return datetime.datetime.fromtimestamp(ms)

  def parse_parse(tm):
    return timedelta(hours=tm[0], minutes=tm[1], seconds=tm[2])

  sec = int(mktime(5, 2, 1))
  
  print(sec)
  print(parse_parse(time(sec)), sep=":")
  
  print(parse_parse(time(mktime(0, 0, 1))))
  print(parse_date(gen_date(10, 2, 3)))
  print(parse_date(gen_date_smart(0, 2, 3)))
  
  
  print(parse_parse(time_until(4, 30)))
  print(parse_parse(time_until_string("7:30")))
  
  print(now(), today_midnight())
  
  while True:
      print(parse_parse(time(now() % mktime(24) - mktime(7))), parse_parse(time_until_string("7:30")), sep="\t")
