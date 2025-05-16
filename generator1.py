def gen():
    yield 1
    yield 2
for i in gen():
    print(i)

n = gen()
print(next(n))
print(next(n))