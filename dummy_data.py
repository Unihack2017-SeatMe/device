import random
import requests
import time

URL = "http://localhost:8080"

def generate_dummy_data(_id, count):
    url = "%s/devices" % URL
    headers = {'Content-Type': 'application/json', }
    params = '{"id":"%s","count":"%s","capacity":"9"}' % (_id, count)

    r = requests.post(url, data=params, headers=headers)

if __name__ == "__main__":
    ids = range(5)
    while True:
        print("Generating...")
        generate_dummy_data(random.choice(ids), random.randint(0,9))
        print("Asdfasdf")
        time.sleep(5)
