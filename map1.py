from functools import reduce

def p(x):
    return x + 5

y = [1,2,3,4,5]

[print(i) for i in map(p, y)]

z = reduce(lambda x,y1 : x+y1, y)
print(z)