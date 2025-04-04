import threading as th
import time 

def task(name, delay):
    print(f"thread: {name}")
    for i in range(3):
        #simular um delay
        time.sleep(delay)

        print(f"thread: {name} executing step {i+1}")