def gen1():
    yield 1
    yield 2
    yield 3

y = gen1()
print(y)
print(list(y))    