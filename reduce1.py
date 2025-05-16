from functools import reduce

def func1(x,y):
    return f"{x}:){y}"

print(list(reduce(func1, [1,2,3,4,5])))