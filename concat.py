object1 = [1,2,3,4,5]
object2 = [6,7,8,9,10]

#for mutable types like lists concatenation can be done in 
#place the original list can be a larger list

object1 = object1 + object2
print(object1)

#for immutable datatypes like tuples and string, 
# contacentation involes creating an entirely new object
# not memory efficient so when making repeat concatenations
#on an immutable type, consider a new data structure entirely



obj1 = (1,2,3)
obj2 = (4,5,6)

obj1 = obj1 + obj2
print(obj1)

#multiplication
str = 'hi'
mystr = str*5
print(mystr)

#modifying in place 
numbers = [1, 2, 3]
print("Before modification:", id(numbers))  # Get memory address
numbers.append(4)  # Modify in place
print("After modification:", id(numbers))  # Memory address stays the same


mynumbers = [1, 2, 3]
print("Before modification:", id(mynumbers))  # Get memory address
new_numbers = mynumbers + [4]  # Creates a new list
print("After modification (new object):", id(new_numbers))  # Memory address is different