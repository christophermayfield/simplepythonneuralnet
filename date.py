import time 
import datetime
import math
#number of seconds passed since Jan 1 1970
current_timestamp = time.time()

#dividing it by the number of seconds in a year to get the number of years
num_years = current_timestamp/31536000
print(current_timestamp)
print(num_years)

current_datetime = datetime.time(hour=20,minute=30,second=25) #830pm and 25 seconds

whatever = datetime.time()
print(whatever)

#date
my_date = datetime.date(2025,3,15) #yesterday (it was currently 2025-3-16)

print(my_date)

#datetime 
dt = datetime.datetime(2023,8,3,5)

#current time 
dt_now = datetime.datetime.now()
print(dt)
print(dt.month)
print(dt_now)

#combine brings together a date object and a time object 
d = datetime.date.today()
t = datetime.time(8)
print(datetime.datetime.combine(d,t))

#to extract a date from the datetime object we can use .date()
w = datetime.datetime.now()
print('the date is ', w.date())

#to extract a time from the datetime object we can use .time()
print('the current time is', w.time())

#replace allows us to replace a particular property of the datetime object 
print('changing the year to [1999] ->', w.replace(1999))



#allows us to format a datetime with a string that we choose
print(w.strftime('%b %d %-I %p')) #Mar 17 time am/pm
print(w.strftime("%a %b %d @%-I %p"))


#parse string - super useful when we have to parse user input
print(w.strptime('27 June 2024','%d %B %Y'))
print(w.strptime('16:00 16/08/2024','%H:%M %d/%m/%Y'))


#calculating the difference between times within delta and time delta

#set an alarm for 1 hour and 30 minutes into the future
alarm = datetime.timedelta(hours = 1, minutes = 30)

#the time when the alarm should go off
alarm_buzzer_time = alarm + datetime.datetime.now()
print(alarm_buzzer_time)


report = datetime.timedelta(days=72)
#lets go back 72 days in the past 

report_start_time = datetime.datetime.now() - report
print(report_start_time)

#lets see how long i've been working for 
started_work = datetime.datetime(2025,3,17,18)
finished_work = datetime.datetime.now()
print(finished_work - started_work)

#5 minutes in the future 
now = datetime.datetime.now()
five_minutes_from_now = now + datetime.timedelta(minutes=5)
print(five_minutes_from_now)


