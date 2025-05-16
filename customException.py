class MyError(Exception):
    def __init__(self, message):
        super().__init__(f"{message}, raise using custom exception")
try:
    raise MyError("Custom Error Raised")
except MyError as e:
    print(e)