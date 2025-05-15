l = [1,2,3,4,5,6,7,8,9, "Mushu"]

print(len(l))

thislist = [x**2 for x in range(300)]

tu = 1,2,3,4,5

#print(l + tu) Doesn't work as we cannot add a list and a tuple
print(l)

print(l | tu)