#Hours to go for a particular time.


import datetime as dt
christmas = dt.datetime(2022, 12, 25)
today = dt.datetime.now()
time_till_christmas = christmas - today
print(time_till_christmas)
days1 = time_till_christmas.days
days2 = days1*24
print(days2)


