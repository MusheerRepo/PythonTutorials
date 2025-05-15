s = 'Hello World, this is a good day'
d = {}
print(d.get('H'))
for i in s:
    if d.get(i):
        d[i] += 1
    else:
        d[i] = 1
print(d)

for i, v in d.items():
    if i == ' ':
        continue
    elif v > 1:
        print(f"{i} : {v}")