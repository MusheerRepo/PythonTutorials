x = open("file.txt", "+at")

print("Printing using read()")
print(x.read())

print("Printing using readline()")
x.seek(0)
print(x.readline())
print(x.readline())
print(x.readline())

print("Printing using readlines()")
x.seek(0)
print(x.readlines())

x.write("Now the file has more content!")

print("Printing using readlines()")
x.seek(0)
print(x.readlines())
x.close()

f = open("myfile.txt", "x")