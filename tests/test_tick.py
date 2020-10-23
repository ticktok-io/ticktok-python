from unittest.mock import MagicMock

import pytest
from busypie import wait, SECOND

from ticktok import Ticktok


@pytest.fixture
def client():
    client = Ticktok()
    yield client
    client.unregister_all()


def test_invoke_callback_on_tick(client):
    one_sec_callback = MagicMock()
    two_sec_callback = MagicMock()
    client.register(name='test-clock', schedule='every.1.seconds', callback=one_sec_callback)
    client.register(name='test-clock', schedule='every.2.seconds', callback=two_sec_callback)
    wait().at_most(4 * SECOND).until(lambda: one_sec_callback.call_count > 1)
    wait().at_most(5 * SECOND).until(lambda: two_sec_callback.call_count > 1)
