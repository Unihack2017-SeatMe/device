import random
import requests
import time

URL = "http://localhost:8080"


def generate_dummy_data(_id, count):
    url = "%s/devices" % URL
    headers = {'Content-Type': 'application/json', }
    params = '{"id":"%s","count":"%s","capacity":"9"}' % (_id, count)

    requests.post(url, data=params, headers=headers)


if __name__ == "__main__":
    ids = range(2, 5)
    cached_counts = [0, 0, 0, 0, 0, 0]
    while True:
        print("Generating...")
        # Generate the ID and COUNT
        _id = random.choice(ids)
        cached_counts[_id] += random.randint(-3, 3)

        # Handle MAX and MINS
        if cached_counts[_id] < 0:
            cached_counts[_id] = 0
        elif cached_counts[_id] > 9:
            cached_counts[_id] = 9

        count = cached_counts[_id]
        generate_dummy_data(_id, count)
        print("id: %s, count: %s" % (_id, count))

        # Wait ~5 Seconds
        time.sleep(5)
