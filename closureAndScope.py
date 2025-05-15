x = 100

def c():
    global x
    x = 100
    print(x)
    x+=1

c()

class Mushu:
    x=10

    def func1(self):
        x = 25
        print(f'Inside function {x}')
        self.x+=1
        
        def func2():
            x = self.x # to use class variable x
            # nonlocal x, to use enclosing x
            # global x, to use global x
            print(x)
            print('Printing global x: ', x)
            self.x+=1

        return func2

y = Mushu()

z = y.func1()

z()
z()
z()

print(x)