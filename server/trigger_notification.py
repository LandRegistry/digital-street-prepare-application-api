import json
import requests

with open('swagger_server/responses/notification_2.json') as json_file:
    notification_2 = json.load(json_file)

response = requests.post('http://localhost:5555/AGL117262', headers={"content-type": "application/json"}, data=json.dumps(notification_2))