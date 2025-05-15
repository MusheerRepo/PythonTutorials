def decorat(f):
    def wrapper():
        print("Executing before the function")
        f()
        print("Executing after the function")
    return wrapper

@decorat
def display():
    print("Hello, World!")
    
display()