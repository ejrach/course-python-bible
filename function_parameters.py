
def about(name,age,likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence

# function with default values. Defaults must be at the end
def about2(name, age, likes = "Python"):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence

# positional arguments, need to be in the order of the function parameter definitions
print(about("Jack", 23, "Python"))

# change the order of the arguments (keyword arguments)
print(about(age = 23, name = "Jack", likes = "Python"))

# With and without defaults
print(about2("Jack", 23))
print(about2("Jack", 23, "Football"))