import threading
import sys
import json
import requests
from smart_vision_api import SmartVisionAPI
from webcam import CaptureDevice

URL = "http://localhost:8080"


def get_count(data):
    objects = data['task']['description']
    print(data['task'])
    return objects.count(u"person")


def post_pedestrian_detection(count):
    url = "%s/devices" % URL
    headers = {'Content-Type': 'application/json', }
    params = '{"id":"%s","count":"%s","capacity":"%s"}' % (1234, count, 30)

    r = requests.post(url, data=params, headers=headers)

def capture():
    print("Capturing image...")
    capture_device = CaptureDevice()
    image = capture_device.capture_frame()

    print("Processing image...")
    smart_vision_api = SmartVisionAPI()

    # -- Local Image from CLI args
    # command = str(sys.argv[1])
    # encoded_image = smart_vision_api.encode_image(command)
    count = get_count(smart_vision_api.process_image(image))

    print("Post to backend...")
    post_pedestrian_detection(count)

    print(count)
    capture()


if __name__ == "__main__":
    capture()
