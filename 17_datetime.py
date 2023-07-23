import datetime as dt
now = dt.datetime.now()
print(dt.datetime.now())

print(dt.date.today())

now = dt.datetime.now()
print(now.strftime("%d-%m-%y"))

x = dt.date(2002,3,26)
y = dt.datetime(2002, 3, 26, 6)
print(x)
print(y)

a = dt.date(2023, 7, 23)
b = dt.date(2002, 3, 26)
end = dt.datetime.now()

print(end - now)
print(a - b)