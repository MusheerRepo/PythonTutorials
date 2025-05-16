def func1(x):
    return x%2 == 0

print(list(filter(func1, [1, 2, 3, 4, 5])))