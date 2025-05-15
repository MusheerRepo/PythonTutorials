x = 'Tanvi Musheer Khan Tanvi Ali'
y = {}
for i in x:
    if y.get(i):
        y[i] = y[i] + 1
    else:
        y[i] = 1 

for i in y.keys():
    print(f'{i} : {y[i]}')