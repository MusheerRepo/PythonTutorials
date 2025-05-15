class Mushu:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Color: {self.color}, Age: {self.age}")

class Child(Mushu):
    def __init__(self, name, color, age):
        super().__init__(name, color, age)

ob = Child('Mushu', 'Black', 5)
ob.display()