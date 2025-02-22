#membership testing in python 
#updating -- again
docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'
"""
if 'tuple' not in docs:
    # do something 
    print('tuple is not here!')
else:
    # do something else
    print('tuple is here!')

"""

fruits = ['apples', 'blueberries', 'eggplant', 'eggplants']
print('apples' in fruits)
print('Blueberries' not in fruits)
print('blueberries' not in fruits)

print('trumper' in docs)
print(docs.count('tuple'))
print(docs.index('tuple'))
print('\n')


print('------- starting nums -------')
print('\n')


nums = range(10)
print(0 in nums)
print(5 in nums)
print(10 in nums)
print(9 in nums)


print("-----starting stepnums------")
print('\n')

stepnums = range(1,10,2)
print(1 in stepnums)
print(2 in stepnums)
print(3 in stepnums)
print(5 in stepnums)

print("-----starting concatenation------")
