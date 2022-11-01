'''
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference)
'''

# Arguments and Parameters
def print_name(name):
    print(name)
    # name is parameter

print_name('Alex') # Alex is argument for function

# Positional and Keyword Arguments
def foo(a,b,c):
    print(a, b, c)

foo(1,2,3) # positional arguments
foo(b=2, a=1, c=3) #keyword arguments

# Default Arguments
def foo2(a, b, c, d=4): # defaults must be at the end
    print(a, b, c, d)

foo2(1,2,3)
foo2(1,2,3,7)

# Variable Length Arguments
def foo3(a,b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo3(1, 2, 3, 4, 5, six=6, seven=7)

# Forced Keyward Arguments
def foo4(a,b, *, c, d):
    print(a, b, c, d)

foo3(1, 2, c=3, d=4)

# Unpacking Arguments
def foo5(a, b, c):
    print(a, b, c)

my_list = [0,1,2]
foo5(*my_list)

my_dict = {'a':1, 'b':2, 'c':3} # keys must match function parameters
foo5(**my_dict)

# Local vs Global Variables
def foo6():
    global number
    x = number
    number = 3
    print('number inside function:',x)

number = 0
foo6()
print(number)

# Parameter Passing
def foo7(a_list): # mutable objects can be changed within a function, but not immutable objects
    a_list.append(4)

my_list = [1,2,3]
foo7(my_list)
print(my_list)