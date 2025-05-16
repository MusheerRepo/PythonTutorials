my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])
my_set.discard(3)
print(my_set)
print(my_set.union({7, 8}))
print(my_set.intersection({5, 6, 9}))

for x in my_set:
    print(x)

print([x for x in my_set])