
print(1,2,3,4,5)

numbers = [1,2,3,4,5]
print(numbers)

print(*numbers)     # the asterisk unpacks the list. 

##################################################
# unpacking the list passed in. Doing this allows us to pass in a variable amount of values
def add(*values):
    total = 0
    for number in values:
        total = total + number
    
    return (total)

print(add(1,2,3,4,5,6,7,8,9))  # all these numbers get packed into a tuple, or list, and get unpacked at the function

##################################################

def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence

dictionary = {"name":"Eric", "age":23, "likes":"Python"}

print(about(**dictionary))  # use ** to unpack dictionary items

##################################################
# a way to put keyword arguments into a dictionary and loop through them

def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))


foo(huda = "female", eric = "male", fred = "male")