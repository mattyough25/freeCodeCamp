# Sets: unordered, mutable, no duplicates
my_set = {1,2,3}
print(my_set)

# No duplicate
my_set_dup = {1,2,3,1,2}
print(my_set_dup)

# 
my_set2 = set("Hello")
print(my_set2)

# Empty set
myset = set()
print(myset)

# Add Elements
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# Remove elements
myset.remove(3)
print(myset)

myset.discard(2)
print(myset)

# Empty set
myset.clear()

# Remove and see index
myset2 = {1,2,3}
myset2.pop()
print(myset2)

# Union and intersection
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i2 = odds.intersection(primes)
print(i2)

# Difference of 2 sets
setA = {1,2,3,4,5,6,7,8,9} 
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

diff2 = setB.symmetric_difference(setA)
print(diff2)

# Modify sets in place
setA.update(setB)
print(setA)

# Intersection update
setA = {1,2,3,4,5,6,7,8,9} 
setB = {1,2,3,10,11,12}

setA.intersection_update(setB)
print(setA)

# Difference update
setA = {1,2,3,4,5,6,7,8,9} 
setB = {1,2,3,10,11,12}

setA.difference_update(setB)
print(setA)

# symmetric difference update
setA = {1,2,3,4,5,6,7,8,9} 
setB = {1,2,3,10,11,12}

setA.symmetric_difference_update(setB)
print(setA)

# Super and is set
setA = {1,2,3,4,5,6} 
setB = {1,2,3}

print(setA.issubset(setB))
print(setB.issubset(setA))

print(setB.issuperset(setA))
print(setA.issuperset(setB))

# Disjoined set
setC = {7,8}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

# Copying sets
setB = setA
print(setB)

setB.add(7)
print(setB)
print(setA)

# use .copy method

# Frozed set
a = frozenset([1,2,3,4]) # cant change
print(a)
