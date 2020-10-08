import pytest

from ticktok.client import Ticktok, ClockRegisterError


def test_fail_on_invalid_schedule():
    with pytest.raises(ClockRegisterError):
        Ticktok().schedule(name='kuku', schedule='every.invalid')
