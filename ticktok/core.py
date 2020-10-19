from threading import Thread

import requests

from ticktok.server import ServerSDK

DEFAULT_DOMAIN = 'http://localhost:9643'
DEFAULT_TOKEN = 'ticktok-zY3wpR'


class Ticktok:

    def __init__(self, url=DEFAULT_DOMAIN, token=DEFAULT_TOKEN):
        self._server = ServerSDK(url, token)
        self._is_running = False
        self._poll_url = None
        self._callback = None

    def register(self, name, schedule, callback):
        clock = self._server.register_clock(name, schedule)
        self._callback = callback
        self._poll_url = clock['channel']['details']['url']
        self._start()

    def _start(self):
        if not self._is_running:
            self._is_running = True
            Thread(target=self.poll_ticks).start()

    def poll_ticks(self):
        while self._is_running:
            if self._poll_url:
                response = requests.get(self._poll_url)
                if response.json():
                    self._callback()

    def unregister_all(self):
        self._is_running = False
        self._callback = None
        self._poll_url = None
