class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __call__(self, rating):
        print(f"{self.title}:{self.author}:{rating}")

obj = Book('Oliver Twist','Oliver')
obj(3)

class Library():
    def __init__(self, name):
        self.name = name
    
    def __len__(self):
        return len(self.name)
obj1 = Library("SSGMCE")    
print(obj1.__len__())

class Calculator():
    def __init__(self, number):
        self.number = number
    def __call__(self, value):
        print(self.number*value)
obj2 = Calculator(5)
obj2(2)

        
    