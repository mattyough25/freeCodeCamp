# Errors and Exceptions

'''
# Syntax error
a = 5 print(a)

# Exception error
a = 5 + '10'

# Raising an exception
x = -5
if x < 0:
    raise Exception('x should be positive')

# Raising exception with assert
x = -5
assert(x>=0),'x is not positive'

# Handle Assertion using try/except
try:
    a = 5/0
except ZeroDivisionError:
    print('Caught Exception')

try:
    a = 5/0
except Exception as e:
    print(e)

try:
    #a = 5/0
    b = 5+'10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else: 
    print('Everything is fine')
finally:
    print('cleaning up...')
'''
# Define own exceptions
from pyexpat.errors import messages


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small',x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)