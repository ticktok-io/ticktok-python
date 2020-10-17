import threading
from threading import Thread

import requests
from requests import HTTPError, ConnectionError

from ticktok.http_session import create_retry_session

DEFAULT_DOMAIN = 'http://localhost:9643'
DEFAULT_TOKEN = 'ticktok-zY3wpR'


class ClockRegisterError(Exception):
    pass


class TicktokClient:

    def __init__(self, url=DEFAULT_DOMAIN, token=DEFAULT_TOKEN):
        self._is_running = False
        self._url = url
        self._token = token
        self._poll_url = None
        self._callback = None
        self._lock = threading.Lock()
        self._http_session = create_retry_session()

    def register(self, name, schedule, callback):
        try:
            response = self._http_session.post(f'{self._url}/api/v1/clocks?access_token={self._token}',
                                     json={'name': name, 'schedule': schedule})
            response.raise_for_status()
            self._callback = callback
            self._poll_url = response.json()['channel']['details']['url']
            self._start()
        except (ConnectionError, HTTPError) as e:
            raise ClockRegisterError(f'Failed to register clock => (name={name}, schedule={schedule})', e)

        callback()

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
