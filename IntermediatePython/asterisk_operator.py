# Multiplication
result = 5 * 7
print(result)

# Power Operator
result = 2 ** 4
print(result)

# Repeat Elements (Tuples, Lists, Strings)
zeros = [0] * 10
print(zeros)

zeros = [0, 1] * 10
print(zeros)

# Args and Kwargs
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)

# Argument Unpacking
def foo2(a, b, c):
    print(a, b, c)

my_list = [0,1,2]
foo2(*my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo2(**my_dict)

# Unpacking Containers
numbers = [1,2,3,4,5,6]

*beginning, last = numbers
print(beginning)
print(last)

numbers = [1,2,3,4,5,6]

beginning, *last = numbers
print(beginning)
print(last)

numbers = [1,2,3,4,5,6]

beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

numbers = [1,2,3,4,5,6]

beginning, *middle, secondlast, last = numbers
print(beginning)
print(middle)
print(secondlast)
print(last)

# Merge Iterables into List
my_tuple = (1, 2, 3)
my_list  = [4, 5, 6]

new_list = [*my_tuple, *my_list]
print(new_list)

my_tuple = (1, 2, 3)
my_set  = {4, 5, 6}

new_list = [*my_tuple, *my_set]
print(new_list)

dict_a = {'a': 1, 'b':2}
dict_b = {'c': 3, 'd':4}

new_dict = {**dict_a, **dict_b}
print(my_dict)