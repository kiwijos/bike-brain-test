#!/usr/bin/env python
#
#

import time
import requests

url = "http://express-server:1337"

def get_data(api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

def insert_data(api, id):
        data = {
            "city_id": id,
            "geoJSON": "hejhej"
        }
        response = requests.post(f"{api}/update", json=data)

        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")


test = 0

while test < 10:
    insert_data(url, test)
    test += 1
    time.sleep(1)

print("slut")
