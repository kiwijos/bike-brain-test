#!/usr/bin/env python
"""
Bike module
"""
import requests
import time
import threading

URL = "http://localhost:1337/eventsource"

class Bike():
    API_URL = "http://localhost:1337/eventsource"

    """
    Class that represents the bike and it's brain (functionality)
    """
    def __init__(self, id):
        """ Constructor """
        self._id = id
        self._status = 0
        self._lat = 18.07458333029719
        self._lng = 59.354737133303125
        self._interval = 2
        self._running = True
        # Set up a thread for the bike loop
        self._thread = threading.Thread(target=self.run_bike)
        self._thread.start()

    def run_bike(self):
        while True:
            data = {
                'status': self._status,
                'id': self._id,
                'lng': self._lng,
                'lat': self._lat
            }
            print(data)
            # self._update_bike_data(data)
            time.sleep(self._interval)


    def set_interval(self, interval):
        self._interval = interval

    def _update_bike_data(self, data):
        response = requests.get(self.API_URL, json=data)
        if response.status_code == 200:
            data = response.json()
            
        else:
            print(f"Errorcode: {response.status}")

    def stop(self):
        self._running = False
        self._thread.join()