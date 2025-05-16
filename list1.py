my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list.extend([5, 6])
print(my_list)

my_list.insert(2, 99)
print(my_list)

my_list.remove(3)
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.index(99))
print(my_list)

print(my_list.count(1))
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

for x in my_list:
    print(x)

v = (print(x) for x in my_list)
print(next(v))