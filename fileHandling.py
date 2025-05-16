with open("test.txt", "w") as f:
    f.write("Hello World")
    f.close()

with open("text1.txt", "at") as f:
    f.write("Hello World")
    f.close()

with open("text1.txt", "r") as f:
    x = f.read()
    print(x)
    f.close()