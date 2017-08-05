import base64
import json
import requests

method_type = 'tagging3'


class SmartVisionAPI:
    @staticmethod
    def encode_image(filename):
        with open(filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string

    @staticmethod
    def post_image(encoded_string):
        cmd_json = {'Content-Type': 'application/json', }
        cmd_params = '{"service":"%s","image":"%s"}' % (method_type, encoded_string)
        cmd_auth = ('demo1', 'hackathon7493')
        cmd_url = "http://smartvision.aiam-dh.com:8080/api/v1.0/tasks"

        r = requests.post(cmd_url, auth=cmd_auth, data=cmd_params, headers=cmd_json)
        res = json.loads(r.text)
        return res['task']['uri'].split('/')[-1]

    @staticmethod
    def put_run_image(file_id):
        cmd_header = {'Content-Type': 'application/json', }
        cmd_data = '{"scanned":true}'
        cmd_url = 'http://smartvision.aiam-dh.com:8080/api/v1.0/tasks/run/' + file_id

        r = requests.put(cmd_url, headers=cmd_header, data=cmd_data, auth=('demo1', 'hackathon7493'))
        return json.loads(r.text)

    def process_image(self, encoded_image):
        file_id = self.post_image(encoded_image)
        return self.put_run_image(file_id)
