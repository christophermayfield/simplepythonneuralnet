rainbow = ['red','orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

print(rainbow[1])

print(rainbow[1:4])

#start value blank, stop value blank, step value of 2 
print(rainbow[::2])

#reverse a sequence with a negative value 
print(rainbow[::-1])

#string slicing 
my_name = 'Christopher'
print(my_name[:3])

numbers = [1,2,3,4,5,6,7,8,9,10]
#number of items in the array 
print(len(numbers))

#minimum values
print(min(numbers))

#max value 
print(max(numbers))

#min value of string - closest to beginning
print(min(my_name))

#max value of string - closest to end 
print(max(my_name))

#lexigraphical ordering - look this up
# numbers are lower than letters
mixed = 'christopher2019'
print(max(mixed))
print(min(mixed))

