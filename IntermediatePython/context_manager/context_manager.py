# Open file
with open('notes.txt','w') as file: # Recommended to open a file
    file.write('some to-do')

file = open('notes2.txt','w') # Not recommended to open a file
try:
    file.write('some todoo')
finally:
    file.close()

# In threading
'''
from threading import Lock
lock = Lock()
lock.aquire()
#.....
lock.release() # Don't use this method

with lock: # Do this with lock in threading
    
    #.....
'''
# Own classes
class ManagedFile:
    def __init__(self, filename):
        self.filename=filename
        print('init')

    def __enter__(self):
        print('enter')
        self.file = open(self.filename,'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        #print('exc:', exc_type, exc_value)
        print('exit')
        return True

with ManagedFile('notes3.txt') as file:
    print('doing some stuff')
    file.write('some to-do')
    file.somemethod()
print('continuing')

# Implimenting with as a function
from contextlib import contextmanager

from regex import F

@contextmanager
def open_managed_file(filename):
    f = open(filename,'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes4.txt') as f:
    f.write('some to-do')