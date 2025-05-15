class Person:
    name = 'Musheer'
        
    def __init__(self, name, age):
        print(self.name)
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)