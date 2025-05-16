def decorate(func):
    def wrapper():
        print("Decorator: Before function call")
        func()
        print("Decorator: After function call")
    return wrapper

@decorate
def func1():
    print("Code of func1")

func1()