# Pendulum is a Python library that is used to ease the datetimes manipulation.
import pendulum


# india time zone
dt_Kolkata = pendulum.datetime(2021, 6, 11, tz='Asia/Kolkata')
print(dt_Kolkata)


# methods to craete nbew datetime instance
new_dt = pendulum.datetime(2021, 6, 11)
print(type(new_dt))

# get the timezone
print(new_dt.timezone.name)

# helper() function autimatically set the timezone to local timeznon
local_tz = pendulum.local(2021, 6, 11)
print(local_tz.timezone.name)

# now() method returns the current date and time.

now = pendulum.now()
print(now)

# get today date
today = pendulum.today()
print(today)

# get yesterday date
yesterday = pendulum.yesterday()
print(yesterday)

# get tomorrow date
tomorrow = pendulum.tomorrow()
print(tomorrow)

# Parsing:- Parsing is the process of parse string date and time to pendulum date time

dt = pendulum.parse('1975-05-21T22:00:00', tz='Asia/Kolkata')
print(type(dt))
print(dt)

print("----------")

# when you pass non-standard string please pass strict=False

dt = pendulum.parse('31-01-01', strict=False)
print(dt)

# Attributes and Properties
#  Python pendulum provide lots of properties and methods rather than default datetime class.

# dt = pendulum.parse('2021-06-18T23:26:11.123789')
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.minute)
# print(dt.second)
# print(dt.day)
# print(dt.day_of_week)
# print(dt.day_of_year)
# print(dt.week_of_year)
# print(dt.week_of_month)
# print(dt.days_in_month)
# print(dt.timestamp())
# print(dt.float_timestamp)
# print(dt.int_timestamp)



# Pendulum provides helpers that return a new instance with some attributes modified compared to the original instance.

dt = pendulum.now()
time = dt.set(year=1975, month=5, day=21).to_datetime_string()
print(time)
print(type(time))

# you can use on() and at() method to change date and time respectively

time = dt.on(1975, 5, 21).at(22, 32, 5).to_datetime_string()
print(time)


time = dt.at(10).to_datetime_string()
print(time)

time = dt.at(12, 30).to_datetime_string()
print(time)

# you can also modify the timezone

tz = dt.set(tz='Asia/Kolkata')
print(tz)


# ---- String formatting 

dt = pendulum.datetime(1975, 12, 25, 14, 15, 16)
print(dt)

print("To date string:- ",dt.to_date_string())
print("To formatted date string:- ", dt.to_formatted_date_string())
print("to time string:- ", dt.to_time_string())
print("to datetime string:- ", dt.to_datetime_string())
print("to day and datetime string:- ", dt.to_day_datetime_string())
