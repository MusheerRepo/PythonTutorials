x = {1:2, "5": 6, 5.09: 7.8}

y = {"t": 7, 8: 9, 10: 11}
z = {1, 2, 3, 4, 5}
print(x[True])

[print(i,v) for i,v in x.items()]

print({**x, **y})

h = [1,2]
k = [3,4]
print(*h, *k, *z)