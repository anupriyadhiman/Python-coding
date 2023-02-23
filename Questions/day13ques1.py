# Days to go for a particular date in the future

import datetime as dt
christmas = dt.datetime(2022, 12, 25)
today = dt.datetime.now()
time_till_christmas = christmas - today
print(time_till_christmas)
print(time_till_christmas.days)
