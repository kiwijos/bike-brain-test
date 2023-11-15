#!/usr/bin/env python
"""
Bike module
"""
import asyncio

class Bike():
    """
    Class that represents the bike and it's brain (functionality)
    """
    def __init__(self, id, sim_data=None):
        """ Constructor """
        self._simulation_data = sim_data
        self._id = id

    async def start_simulation(self, url, session):
        for trip in self._simulation_data['trips']:
            for position in trip:
                data_to_send = {
                    "id": self._id,
                    "geometry": position
                }
                await self._update_bike_data_async(session, url, data_to_send)
                await asyncio.sleep(2)

    async def _update_bike_data_async(self, session, api, data):
        async with session.post(f"{api}/update", json=data) as response:
            if response.status == 200:
                response_data = await response.json()
                print(response_data)
            else:
                print(f"Errorcode: {response.status}")
