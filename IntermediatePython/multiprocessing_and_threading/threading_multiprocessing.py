## Speed up code

'''
## Multiprocessing
from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()
#print(num_processes)

# Create process
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# Start processes
for p in processes:
    p.start()

# Join
for p in processes:
    p.join()

print('end main')

'''

## Multi-threading
from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

threads = []
num_threads = 10
#print(num_processes)

# Create thread
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# Start thread
for t in threads:
    t.start()

# Join
for t in threads:
    t.join()

print('end main')
