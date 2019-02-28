
a = 250

def f1():
    global a    # indicates I'm going to change the global variable 'a'
    a = 100
    print(a)

def f2():
    a = 50      # local
    print(a)

f1()
f2()
print(a)




