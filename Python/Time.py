import time
import calendar

ticks = time.time()
print("Number of ticks since 1/1/70 ate midnight: ", ticks)


localtime = time.localtime(time.time())
print("Localdate: ", localtime)

formatedtime = time.asctime(time.localtime(time.time()))
print("Formated time: ", formatedtime)

cal = calendar.month(2022, 2)
print("Calendar: ", cal)