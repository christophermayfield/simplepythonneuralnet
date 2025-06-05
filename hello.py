

#simply prints the name
def print_name():
    print("hello chris")
def packer(*args):
    for val in args:
        print(val)


def two_plus_two():
    val = 2 + 2
    return val

def packer2(*args):
    print(args)
def calculate_total(*args):
    total = sum(args)
    return total
def unpacker():
    return (1,2,3)
var1,var2,var3 = unpacker()
print('the first value is',var1)
print('the second value is',var2)
print('the third value is',var3)

packer('my','homie',55)
packer2('my', 'homie', 55)
print(calculate_total(1,0,5098534098))


#print("the result is",add_two_with_two_nums(1,599))


