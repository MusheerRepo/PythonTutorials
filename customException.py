class FakeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"{self.message} raised from customException.py")

def raise_fake_exception():
    raise FakeException("This is a fake exception for testing purposes,")

raise_fake_exception()