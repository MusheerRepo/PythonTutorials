def iterator(n):
    i = 0

    def next():
        nonlocal i
        x = n[i]
        i += 1
        return x
    return next

i = iterator([1,2,3,4,5])
print(i())
print(i())
print(i())