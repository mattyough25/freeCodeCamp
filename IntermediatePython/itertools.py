# itertools: product, permutations, combinations, accumulate, groupby, infinite iterators

# Product
from itertools import product
a = [1,2]
b = [3]
prod = product(a,b)
print(list(prod))
prod = product(a,b,repeat = 2)
print(list(prod))

# Permutation
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))
perm = permutations(a,2)
print(list(perm))

# Combinations
from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))
comb = combinations_with_replacement(a,2)
print(list(comb))

# Accumulate
from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))
a = [1,2,5,3,4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

# Group By
from itertools import groupby

a = [1,2,3,4]
group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
            {'name': 'Lisa', 'age': 27},{'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# Infinite Iterators
from itertools import count, cycle, repeat

# Count
for i in count(10):
    print(i)
    if i == 15:
        break

# Cycle
a = [1,2,3]
count = 0
for i in cycle(a):
    print(i)
    count = count + 1
    if count == 20:
        break

# Repeat
for i in repeat(1, 10):
    print(1)