#!/usr/bin/env python
"""
Bike module
"""
import threading
import json
from sseclient import SSEClient

class SSEListener():
    """
    Class for listening to events
    """
    URL = "http://localhost:1337/eventsource"

    def __init__(self, bike_instance):
        self._bike = bike_instance
        self.thread = threading.Thread(target=self.listen)
        self.thread.start()

    def listen(self):
        try:
            for event in SSEClient(self.URL):
                data = json.loads(event.data)
                print(data['id'])
        except Exception as e:
            print(f"Error in SSE connection: {e}")
