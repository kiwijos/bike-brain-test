#!/usr/bin/env python
"""
Bike module
"""
import requests
import time
import threading
import geopy # Will try this to send positions

class Bike():
    API_URL = 'http://express-server:1337/bikes/'

    """
    Class that represents the bike and it's brain (functionality)
    """
    def __init__(self, id, data):
        """ Constructor """
        self._id = id
        self._status = 0
        self._lat = data['initialStart'][0]
        self._lng = data['initialStart'][1]
        self._interval = 2
        self._simulations = data['trips']
        self._running = True

        # Set up a thread for the bike loop
        self._thread = threading.Thread(target=self.run_bike)
        self._thread.start()

    @property
    def id(self):
        return self._id

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, interval):
        self._interval = interval

    def get_data(self):
        return {
            'id': self.id,
            'status': self._status,
            'lat': self._lat,
            'lng': self._lng
        }

    def run_bike(self):
        while self._running:
            data = self.get_data()
            self._update_bike_data(data)

            time.sleep(self._interval)

    def run_simulation(self):
        for trip in self._simulations:
            for position in trip:
                self._lat = position[0]
                self._lng = position[1]
    
                self._update_bike_data(self.get_data())
                time.sleep(2)

    def _update_bike_data(self, data):
        response = requests.post(self.API_URL, json=data)
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Errorcode: {response.status_code}")

    def start(self):
        self._running = True
        self._thread.start()

    def stop(self):
        self._running = False
        self._thread.join()
