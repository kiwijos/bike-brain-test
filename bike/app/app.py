#!/usr/bin/env python
#
#

import os
import json
import asyncio
import aiohttp
from src.bike import Bike

url = "http://express-server:1337"
# url = "http://localhost:1337"

def load_json_from_directory(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data.append(json.load(file))
    return data

async def main(data):
    bike_id = [
        'GOGOGO',
        'REG123',
        '123REG',
        'HEJHEJ',
        'TEST12'
    ]
    bikes = []

    for i, id in enumerate(bike_id):
        bikes.append(Bike(id, data[i]))

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(bike.start_simulation(url, session)) for bike in bikes]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    directory = './routes'
    json_data = load_json_from_directory(directory)

    asyncio.run(main(json_data))
