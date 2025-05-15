def gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

x = gen()
print(x)
print(next(x))
print(next(x))
print("Hello")
print(next(x))