def person(name, age):
    print(name, age)
person("Alice", age=30)

def car(*engine, **color):
    print(engine)
    print(color)

car("v6", "v8", color="red", year=2020)