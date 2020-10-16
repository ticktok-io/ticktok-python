import pytest

from tests import ticktok_server
from ticktok import ClockRegisterError, TicktokClient


@pytest.fixture
def client():
    client = TicktokClient()
    yield client
    client.unregister_all()


def test_fail_on_invalid_schedule(client):
    with pytest.raises(ClockRegisterError):
        client.register(name='kuku', schedule='every.invalid', callback=lambda: True)


def test_register_a_new_clock(client):
    clock = {'name': 'test-clock', 'schedule': 'every.30.seconds'}
    client.register(**clock, callback=lambda: True)
    ticktok_server.has_clock_with(**clock)


def test_fail_on_invalid_connection_details():
    with pytest.raises(ClockRegisterError):
        TicktokClient(url='http://unknown').register(name='kuku', schedule='every.1.seconds', callback=lambda: True)
    with pytest.raises(ClockRegisterError):
        TicktokClient(token='invalid-token').register(name='kuku', schedule='every.1.seconds', callback=lambda: True)
