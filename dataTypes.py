x = range(3)
print(type(tuple(x)))

args = [0, 6, 1]
r = range(*args)
print(list(r)) 

y = list(x)
print(range(*y))

print(memoryview(b'abcdefghijklmnopqrstuvwxyz'))
print(memoryview(b'abcdefghijklmnopqrstuvwxyz').hex())
print(memoryview(b'abcdefghijklmnopqrstuvwxyz').shape)
print(memoryview(b'abcdefghijklmnopqrstuvwxyz').tolist())