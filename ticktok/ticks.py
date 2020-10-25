from threading import Thread
from time import sleep

import requests


class Ticker:

    def __init__(self):
        self._consumers = {}
        self._is_running = False

    def register(self, url, callback):
        self._consumers[url] = callback

    def start(self):
        if not self._is_running:
            self._is_running = True
            Thread(target=self.poll_ticks).start()

    def poll_ticks(self):
        while self._is_running:
            consumers = self._consumers.copy()
            for url, callback in consumers.items():
                response = requests.get(url)
                if response.json():
                    Thread(target=callback).start()
                sleep(0.01)

    def unregister_all(self):
        self._is_running = False
        self._consumers.clear()
