# lambda arguments: expression

# Lambda Function
add10 = lambda x: x + 10

# Normal Function
def add10n(x):
    return x + 10

print(add10(5))
print(add10n(5))

# Multiple arguments
mult = lambda x,y: x * y

print(mult(2,3))


# Used within sorted()
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)
points2D_sorted_lambda = sorted(points2D, key = lambda x: x[1])
print(points2D_sorted_lambda)

# Used within map()
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

# for loop does the same thing
c = [x*2 for x in a]
print(c)

# Used within filter()
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2 == 0,a)
print(b)

# for loop does the same thing
c = [x for x in a if x%2==0]
print(c)

# Used within reduce()
from functools import reduce
a = [1,2,3,4,5,6]
product_a = reduce(lambda x,y: x*y,a)
print(product_a)

