from ticktok.client import Ticktok


class TestTicktok(object):

    def test_hello(self):
        assert 'Hello' in Ticktok().say_hello()

    def test_should_fail_on_invalid_schedule(self):
        # 1. start a ticktok mock (http server)
        # 2. call the create clock function
        # 3. verify the mock server got the correct body
        # 4. validate invalud schedule exception
        pass
