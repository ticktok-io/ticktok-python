import threading
from contextlib import contextmanager

import pytest

from ticktok import TicktokClient


@pytest.fixture
def client():
    client = TicktokClient()
    yield client
    client.unregister_all()


def test_invoke_callback_on_tick(client):
    with verify_callback_invoked() as callback:
        client.register(name='test-clock', schedule='every.1.seconds', callback=callback)


@contextmanager
def verify_callback_invoked():
    e = threading.Event()

    def callback():
        e.set()

    yield callback
    e.clear()  # Make sure callback is called asynchronously
    e.wait(timeout=10)
    assert e.isSet()
