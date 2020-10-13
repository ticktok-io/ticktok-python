class ClockRegisterError(Exception):
    pass


class Ticktok:

    def register(self, name, schedule, callback):
        raise ClockRegisterError()
