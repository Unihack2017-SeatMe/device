import sys

from smart_vision_api import SmartVisionAPI

URL = "http://192.198.0.2:8080"

def get_count(data):
    objects = data['task']['description']
    return objects.count(u"person")


def post_pedestrian_detection(count):
    url = "%s/devices" % URL
    headers = {'Content-Type': 'application/json', }
    params = '{"id":"%s","count":"%s","capacity":"%s"}' % (1234, count, 30)

    r = requests.post(url, data=params, headers=headers)
    res = json.loads(r.text)
    return res


if __name__ == "__main__":
    smart_vision_api = SmartVisionAPI()
    command = str(sys.argv[1])
    encoded_image = smart_vision_api.encode_image(command)
    count = get_count(smart_vision_api.process_image(encoded_image))

    print(count)
