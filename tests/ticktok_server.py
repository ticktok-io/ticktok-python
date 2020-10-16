import requests
from hamcrest import assert_that, has_item, has_entries

DEFAULT_TOKEN = 'ticktok-zY3wpR'


def has_clock_with(name, schedule):
    response = requests.get(f'http://localhost:9643/api/v1/clocks?access_token={DEFAULT_TOKEN}')
    response.raise_for_status()
    assert_that(response.json(), has_item(
        has_entries(name=name, schedule=schedule)
    ))
