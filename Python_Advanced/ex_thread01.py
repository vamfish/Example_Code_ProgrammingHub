import threading
import time
from queue import Queue

print_lock = threading.Lock()
q = Queue()

def func(y):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name, y)

def threader():
    while True:
        y = q.get()
        func(y)
        q.task_done

# 10 threads to do some JOB
for x in range(10):
    #defining the thread.
    t = threading.Thread(target=threader)
    #will die when main thread dies
    t.daemon = True
    t.start()

start = time.time() # starting time
for y in range(20):
    q.put(y)

q.join() # will wait until the thread terminates
print("Entire time took:", time.time()-start)