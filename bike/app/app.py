#!/usr/bin/env python
"""
Alt program for bikes, using eventsource
"""
import os
import json
from src.bike import Bike
from src.sselistener import SSEListener

def load_json_from_directory(directory):
    """ Function that loads all the json files from directory """
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            id = filename[:-5] # Remove .json
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data[id] = (json.load(file)) # Save into dict with filename as key (id)
    return data

if __name__ == "__main__":
    # Load all .json files from directory
    directory = './routes'
    json_data = load_json_from_directory(directory)
    bikes = []
    listeners = []

    # Create all bikes based on files in folder ./routes and start the program in every bike
    for key, value in json_data.items():
        id = key
        data = value
        bikes.append(Bike(id, data))

    # Wrap each bike with a listener that gives the bike instructions based on SSE from a url
    for bike in bikes:
        listeners.append(SSEListener(bike))
