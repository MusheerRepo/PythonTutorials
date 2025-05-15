class Mushu:
    def beforeMarriage(self):
        print("Mushu was single but happy")

def afterMarriage(self):
    print("Mushu is married and even more happy")

def afterMarriage1(self):
    print("Mushu is married and even more happy and living his life to the fullest")

ob = Mushu()
ob.beforeMarriage()


Mushu.beforeMarriage = afterMarriage
ob.beforeMarriage()
