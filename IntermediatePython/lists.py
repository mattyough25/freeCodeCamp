# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry","apple"]
print(mylist)

mylist2 = list()
print(mylist2)

mylist3 = [5, True, "apple", "apple"]
print(mylist3)

# Retrieving a value from a list
item = mylist[2]
print(item)

# Retrieving a value starting from the end
item2 = mylist[-1]
print(item)

# Iterate through list
for i in mylist:
    print(i)

# Check for value
if "banana" in mylist:
    print("yes")
else:
    print("no")

# Number of Elements in list
length = len(mylist)

# Add values
mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

# Remove values
item_remove = mylist.pop()
print(item_remove)
print(mylist)

mylist.remove("cherry")
print(mylist)

mylist.clear()
print(mylist)

# Reverse list order
print(mylist.reverse)

# sort list
numlist = [4,3,1,-1,-5,10]
numlistsort = numlist.sort()
#print(numlistsort)

new_list = sorted(numlist)
print(new_list)

# New lists of 5 zeros
newlist = [0] * 5
print(newlist)

# Concatenate lists
list = [1,2,3,4,5]
concatlist = list + newlist
print(concatlist)

# Slicing
slice_list = [1,2,3,4,5,6,7,8,9]
slice_list2 = slice_list[1:5]
print(slice_list2)

# Step indexing
slice_list3 = [1,2,3,4,5,6,7,8,9]
slice_list4 = slice_list3[::3]
print(slice_list4)

# Reverse List
reverse_list = [1,2,3,4,5,6,7,8,9]
reverse_list2 = reverse_list[::-1]
print(reverse_list2)

# Copying
list_org = ["banana","cherry","apple"]

# list_cpy = list_org Dont do this. 

#list_cpy = list_org.copy
#list_cpy2 = list(list_org)
list_cpy = list_org[:]

list_cpy.append("lemon")

print(list_cpy)
print(list_org)

# List comprehension
a = [1,2,3,4,5,6]
b = [i*i for i in a]

print(a)
print(b)