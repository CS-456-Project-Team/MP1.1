from threading import Thread
import requests
import random
import time

HOST = '0.0.0.0'
PORT = 8008

def start():
    t = Thread(target=heartbeat)
    t.start()
    calculate()

def heartbeat():
    while True:
        response = requests.get('http://' + HOST + ':' + str(PORT))
        time.sleep(10)
  
def calculate():
    x = 155668381
    while True:
        rand = random.randint(0, x)
        value = x / rand
        print(value)

if __name__ == "__main__":
    start()
