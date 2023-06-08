class Rectangle:
    def __init__(self, a, b):
        self.width = a
        self.height = b

    def getArea(self):
        return self.width * self.height

class Square:
    def __init__(self, a):
        self.a = a

    def getAreaSquare(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

    def getAreaCircle(self):
        pi = 3.14
        return pi * self.r ** 2