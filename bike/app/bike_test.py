#!/usr/bin/env python
"""
Alt program for bikes, using eventsource
"""
from alt_src.bike import Bike
from alt_src.sselistener import SSEListener

if __name__ == "__main__":
    bike_instance = Bike(1)
    sse_listener = SSEListener(bike_instance)
