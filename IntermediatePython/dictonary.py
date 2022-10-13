# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Matt", "age": 26, "city": "Pittsburgh"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

# Access Value
value = mydict["name"]
print(value)

# Change Items
mydict["email"] = "mgyough@gmail.com"
print(mydict)

mydict2["name"] = "Max"
print(mydict2)

del mydict2["age"]
print(mydict2)

# See if item is in dictionary
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("Error")

# Loop through dictionary
for key in mydict:
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

# Copy dictionary
#mydict_cpy = mydict
#print(mydict_cpy) # modifying one changes both

mydict_cpy = mydict.copy()
print(mydict_cpy)

mydict_cpy = dict(mydict)
print(mydict_cpy)

# Merge dictionary
mydict.update(mydict2)
print(mydict)

# Tuple as key
mytuple = (8,7)
mydict_tup = {mytuple:15}
print(mydict_tup)
