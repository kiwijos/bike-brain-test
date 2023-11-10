#!/usr/bin/env python
#
#

import time
import requests
import json

url = "http://express-server:1337"
# url = "http://localhost:1337"


file = open('./routes/1.json')

data = json.load(file)

def update_bike_data(api, data):
        response = requests.post(f"{api}/update", json=data)

        print(response)

        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Errorcode: {response.status_code}")

for trip in data['trips']:
    for position in trip:
        data_to_send = {
            "id": "GOGOGO",
            "geometry": json.dumps(position)
        }
        update_bike_data(url, data_to_send)
        
        time.sleep(5)
