x = 10
def outer():
    x = 20
    def inner():
        nonlocal x
        x = 30
    inner()
    print(x)
outer()

print(x)