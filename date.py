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


/Users/christophermayfield/Library/Messages/Attachments/86/06/5C4A857D-8021-4EA9-BEF5-C21FB84CD233/76403641474__AFDC04BE-72D1-454E-AD6D-BC1A562338EF.heic