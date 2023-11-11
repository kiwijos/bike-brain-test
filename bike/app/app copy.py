#!/usr/bin/env python
#
#

import time
import json
import asyncio

url = "http://express-server:1337"
# url = "http://localhost:1337"


file = open('./routes/2.json')

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
            "geometry": position
        }
        update_bike_data(url, data_to_send)        

        time.sleep(10)

# async def route_loop_2():
#     for i in range(10):
#         print("Loop 2 iteration", i)
#         await asyncio.sleep(0.1)  # Simulate I/O operation

# async def main():
#     task1 = asyncio.create_task(loop1())
#     task2 = asyncio.create_task(loop2())

#     # Wait until both tasks are completed
#     await task1
#     await task2


