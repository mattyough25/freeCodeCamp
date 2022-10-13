# Strings: ordered, immutable, text representation
my_string = "I'm a programmer"
print(my_string)

my_string2 = 'Hello World'
print(my_string2)

# Multiple lines
my_string3 = """Hello
World"""
print(my_string3)

# Access Characters
my_string4 = "Hello World"
char = my_string[0]
print(char)

substring = my_string[1:5]
print(substring)

# Reverse String
substring2 = my_string4[::-1]
print(substring2)

# Combine
greeting = "Hello"
name = "Tom"
sentence = greeting+" "+name
print(sentence)

# Iterate through
for i in greeting:
    print(i)

# Check for character/substrings
if 'e' in greeting:
    print('yes')
else:
    print('no')

# Remove white space
my_string = '   Hello World   '
my_string = my_string.strip()
print(my_string)

# Convert to uppercase
print(my_string.upper())

# Convert to lowercase
print(my_string.lower())

# Find if starts with letter/substring
print(my_string.startswith('H'))

# Find if ends with letter/substring
print(my_string.endswith('d'))

# Find index of character/substring
print(my_string.find('Hello'))

# Count instances
print(my_string.count('l'))

# Replace characters/substring
print(my_string.replace('World','Universe'))

# Convert to list
my_string = 'how are you doing'
my_list = my_string.split(' ')
print(my_list)

# List to string
from timeit import default_timer as timer

new_string = ' '.join(my_list)
print(new_string)

my_list_ = ['a']*1000000
print(my_list)

# bad
start = timer()
my_string = ''
for i in my_list:
    my_string+=i
stop = timer()
#print(my_string)
print(stop-start)

# good
start = timer()
my_string = ''.join(my_list)
stop = timer()
#print(my_string)
print(stop-start)

# Formatting String
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 3
my_string = "the variable is %d" % var
print(my_string)

var = 3.145678
my_string = "the variable is %.2f" % var
print(my_string)

var = 3.145678
my_string = "the variable is {}".format(var)
print(my_string)

var = 3.145678
my_string = "the variable is {:.2f}".format(var)
print(my_string)

var = 3.145678
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var,var2)
print(my_string)

var = 3.145678
var2 = 6
my_string = f"the variable is {var} and {var2}" # Best way to format strings
print(my_string)

var = 3.145678
var2 = 6
my_string = f"the variable is {var*2} and {var2}" # Best way to format strings
print(my_string)