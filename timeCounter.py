def check():
    global year, month, day, hour, min, sec
    if sec>59:
        tmp = sec/60
        sec  = sec%60
        min += tmp

    if min>59:
        tmp = min/60
        min = min%60
        hour += tmp

    if hour>23:
        tmp = hour/24
        hour  = hour%24
        day += tmp

    while (day>31):
        if month in greaterMonth:
            if day>31:
                day -= 31
                month += 1
        else:
            if day>30:
                day -= 30
                month += 1
    if (day==31 and month not in greaterMonth):
        day -= 30
        month += 1
    
    if month>12:
        tmp = month/12
        month = month%12
        year += tmp

x = input("start time: ")
y = input("gone time: ")
x = x.split(" ")
y = y.split(" ")
greaterMonth = [1, 3, 5, 7, 8, 10, 12]
year, month, day, hour, min, sec = x
year = int(year)
month = int(month)
day = int(day)
hour = int(hour)
min = int(min)
sec = int(sec)
gDay, gHour, gMin = y
gDay = int(gDay)
gHour = int(gHour)
gMin = int(gMin)
min += gMin
hour += gHour
day += gDay
check()

print("%d年%d月%d日%d點%d分%d秒" % (year, month, day, hour, min, sec))