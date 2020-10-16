from urllib.error import HTTPError

import requests


def register_clock(name, schedule):
    try:
        response = requests.post(f'{self._url}/api/v1/clocks?access_token={self._token}',
                                 json={'name': name, 'schedule': schedule})
        response.raise_for_status()
    except (ConnectionError, HTTPError) as e:
        raise ClockRegisterError(f'Failed to register clock => (name={name}, schedule={schedule})', e)