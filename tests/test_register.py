import pytest



# ticktok = Ticktok(url, token)
#
#
# ticktok.consumer()
# ticktok.api()
#
# # 1st Option
# ticktok.register(name='kuku', schedule='every.invalid', lambda: True)
#
#
# ticktok.unregister(name='kuku', schedule='every.invalid', lambda: True)
#
#
#
#
#
# # 1st Option
# @ticktok.listen_on(name='kuku', schedule='every.invalid')
# def send_spam(tick_message, clock):
#     pass
#
#
# @ticktok.listen_on(name='kuku', schedule='every.invalid')
# @ticktok.listen_on(name='kuku', schedule='every.invalid2')
# def send_spam1(tick_message, clock):
#     pass
#
# ticktok.tick(clock(name='kuku', schedule='every.invalid'))
# ticktok.tick(tag(name='kuku'))
#
#
# ticktok.pause(name='kuku', schedule='every.invalid')
# ticktok.resume(name='kuku', schedule='every.invalid')
#
#
#
# ticktok.tick_tag(name='saddf')
# ticktok.create_tag(name='saddf')
# ticktok.delete_tag(name='saddf')
#
#
#
# ticktok.clock(name='kuku', schedule='every.invalid').pause()
# ticktok.clock(name='kuku', schedule='every.invalid').resume()
#
# ticktok.tag(name='event').create(at=later())
# ticktok.tag(name='event').delete()
from ticktok.client import ClockRegisterError, Ticktok


def test_fail_on_invalid_schedule():
    with pytest.raises(ClockRegisterError):
        Ticktok().register(name='kuku', schedule='every.invalid', callback=lambda: True)

        #
        # ticktok.register(name='kuku1', schedule='every.invalid', lambda: True)
        #
        #
        # ticktok.clock(name='kuku', schedule='every.invalid').unregister(lambda: True)
        # ticktok.unsubscribe(name='kuku', schedule='every.invali' ,lambda: True)
        #
        # clock.unregister(lambda: True)
        #
        # ticktok.unregister_all()
        #
        #
        # clock.tick()
        #
        # ticktok.clock(name='email-service', schedule='every.invalid').pause()
        #
        # ticktok.register_clock(name='kuku', schedule='every.invalid').register(lambda: True)
        #
        # ticktok.clock(name='kuku', schedule='every.invalid').tick()
        #
        # ticktok.tag(name='event').create(at=)
