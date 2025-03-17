import time 
import datetime
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

#calculating the difference between times within delta and time delta
