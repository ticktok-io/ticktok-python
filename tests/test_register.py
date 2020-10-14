import pytest

from ticktok.client import ClockRegisterError, Ticktok


def test_fail_on_invalid_schedule():
    with pytest.raises(ClockRegisterError):
        Ticktok().register(name='kuku', schedule='every.invalid', callback=lambda: True)
