from threading import Thread

import requests

from ticktok.server import ServerSDK

DEFAULT_DOMAIN = 'http://localhost:9643'
DEFAULT_TOKEN = 'ticktok-zY3wpR'


class Ticktok:

    def __init__(self, url=DEFAULT_DOMAIN, token=DEFAULT_TOKEN):
        self._server = ServerSDK(url, token)
        self._is_running = False
        self._consumers = {}
        self._callback = None

    def register(self, name, schedule, callback):
        clock = self._server.register_clock(name, schedule)
        self._consumers[clock['channel']['details']['url']] = callback
        self._start()

    def _start(self):
        if not self._is_running:
            self._is_running = True
            Thread(target=self.poll_ticks).start()

    def poll_ticks(self):
        while self._is_running:
            consumers = self._consumers.copy()
            for u, c in consumers.items():
                response = requests.get(u)
                if response.json():
                    c()

    def unregister_all(self):
        self._is_running = False
        self._consumers.clear()
