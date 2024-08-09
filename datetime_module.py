import datetime

print(datetime.datetime.now())
now = datetime.datetime.now()
year = now.strftime("%Y %m %d")
time = now.strftime("%I %M %p")
time1 = now.strftime("%H %M %p")

print(year)
print(time)
print(time1)

print(datetime.datetime(2023,4,18))