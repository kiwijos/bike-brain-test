#!/usr/bin/env python
#
#

import os
import json
import asyncio
import aiohttp

# url = "http://express-server:1337"
url = "http://localhost:1337"

file = open('./routes/2.json')

data = json.load(file)

async def update_bike_data_async(session, api, data):
    async with session.post(f"{api}/update", json=data) as response:
        print(response)
        if response.status == 200:
            response_data = await response.json()
            print(response_data)
        else:
            print(f"Errorcode: {response.status}")

async def process_trip(session, url, simulation):
    for trip in simulation['trips']:
        for position in trip:
            data_to_send = {
                "id": "GOGOGO",
                "geometry": position
            }
            await update_bike_data_async(session, url, data_to_send)
            await asyncio.sleep(2)

def load_json_from_directory(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data.append(json.load(file))
    return data

async def main(data):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(process_trip(session, url, simulation)) for simulation in data]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    directory = './routes'
    json_data = load_json_from_directory(directory)

    asyncio.run(main(json_data))
