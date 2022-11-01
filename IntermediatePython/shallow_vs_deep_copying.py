# Assignment Operator
org = [0,1,2,3,4]
cpy = org #This only creates a copy of a reference
cpy[0] = -10
print(cpy)
print(org)

import copy
# shallow copy: one level deep, only references of nested child objects
# deep copy: full independent copy

#Shallow Copy
org = [0,1,2,3,4]
cpy = copy.copy(org) 
cpy[0] = -10
print(cpy)
print(org)

org = [0,1,2,3,4]
cpy = org.copy() 
cpy[0] = -10
print(cpy)
print(org)

org = [0,1,2,3,4]
cpy = list(org) 
cpy[0] = -10
print(cpy)
print(org)

org = [0,1,2,3,4]
cpy = org[:] 
cpy[0] = -10
print(cpy)
print(org)

# Deep Copying (Nested Elements)
org = [[0,1,2,3,4],[5,6,7,8,9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)

class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age

class Company:
    def __init__(self,boss,employee):
        self.boss=boss
        self.employee=employee

p1 = Person('Matt',26)
p2=p1

p2.age = 28
print(p2.age)
print(p1.age)

p1 = Person('Matt',26)
p2=copy.copy(p1)

p2.age = 28
print(p2.age)
print(p1.age)

p1 = Person('Matt',26)
p2=Person('Joe',27)

company = Company(p1,p2)
company_clone = copy.deepcopy(company)

company_clone.boss.age = 28
print(company_clone.boss.age)
print(company.boss.age)

