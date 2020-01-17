import math
# ideas for formatter

def gen(hours, seconds, minutes):
    return (hours   * 60**2
          + seconds * 60**1
          + minutes * 60**0)

sec = gen(61, 65, 1)

def parse(secondsIn):
    secondsOut = secondsIn % 60
    minutes = secondsIn // 60

    minutesOut = minutes % 60

    hoursOut = minutes // 60

    print(f"remaining seconds: {hoursOut}")

    return (hoursOut, minutesOut, secondsOut)

print(sec)
print(*parse(sec))