class Test:
    def method(self):
        print("Original")

obj = Test()

def new_method(self):
    print("Patched")

Test.method = new_method
obj.method()
