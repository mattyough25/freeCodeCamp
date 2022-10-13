# Tuple: ordered, immutable, allows duplicate elemenst

mytuple = ("Max", 28, "Boston")
print(mytuple)

# One element tuple
onetuple = ("Max",)
print(onetuple)

# tuple function
funtuple = tuple(["Max", 28, "Boston"])
print(funtuple)

# Access elements
item = mytuple[0]
print(item)

item2 = mytuple[-1]
print(item2)

# Iterate tuple
for i in mytuple:
    print(i)

# Check for elemenst
if "Max" in mytuple:
    print("yes")
else:
    print("no")

## Tuple Functions
mytuple2 = ('a','p','p','l','e')

print(len(mytuple2))

print(mytuple2.count('p'))

print(mytuple2.index('p'))

mylist = list(mytuple2)
print(mylist)

mytuple3 = tuple(mylist)
print(mytuple3)

#slicing
a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]
print(b)

c = a[::2]
print(c)

d = a[::-1] #reverses tuple
print(d)

#picking
name, age, city = mytuple
print(name)
print(age)
print(city)

i1, *i2, i3 = a
print(i1)
print(i3)
print(i2)

# Working with a tuple can be more efficient because it is immutable
import sys
import timeit
my_list = [0,1,2,"hello",True]
my_tuple = (0,1,2,"hello",True)
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")

print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000))

