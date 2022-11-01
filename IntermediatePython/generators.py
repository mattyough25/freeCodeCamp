def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g)

# Looping through
#for i in g:
    #print(i)

# Using next to go through
'''
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)
'''

# Sum of the outputs
#print(sum(g))

# Sort outputs
#print(sorted(g))

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))

# Efficiency example
from re import A
import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num+=1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num+=1

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))

# Fibonacci Example
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a ,b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

# Generator Expressions
import sys
mygenerator = (i for i in range(100000) if i%2 == 0)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(100000) if i%2 == 0]
print(sys.getsizeof(mylist))