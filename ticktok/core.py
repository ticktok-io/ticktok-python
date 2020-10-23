from ticktok.server import ServerSDK
from ticktok.ticks import Ticker

DEFAULT_DOMAIN = 'http://localhost:9643'
DEFAULT_TOKEN = 'ticktok-zY3wpR'


class Ticktok:

    def __init__(self, url=DEFAULT_DOMAIN, token=DEFAULT_TOKEN):
        self._server = ServerSDK(url, token)
        self._ticker = Ticker()

    def register(self, name, schedule, callback):
        clock = self._server.register_clock(name, schedule)
        self._ticker.register(clock['channel']['details']['url'], callback)
        self._ticker.start()

    def unregister_all(self):
        self._ticker.unregister_all()
