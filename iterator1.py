def iterator(y):
    x = 0
    def next():
        nonlocal x
        z = y[x]
        x += 1
        return z
    return next

j = iterator([1, 2, 3])
print(j())
print(j())
print(j())