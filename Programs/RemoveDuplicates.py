s = 'Hello World, this is a good day'
y = set()

s1 = ''
for i in s:
    y.add(i)
for i in y:
    print(i, end=' ')
print()
for i in s:
    if i not in s1:
        s1 += i
print(s1)

h = "K"
k = "H"

h, k = k, h
print(h, k)