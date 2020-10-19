import requests
from requests import HTTPError, ConnectionError


class ClockRegisterError(Exception):
    pass


class ServerSDK:

    def __init__(self, url, token):
        self._url = url
        self._token = token
        self._http_session = requests.session()

    def register_clock(self, name, schedule):
        try:
            response = self._http_session.post(f'{self._url}/api/v1/clocks?access_token={self._token}',
                                               json={'name': name, 'schedule': schedule})
            response.raise_for_status()
            return response.json()
        except (ConnectionError, HTTPError) as e:
            raise ClockRegisterError(f'Failed to register clock => (name={name}, schedule={schedule})', e)
