'''OOP 

'''


import math

class Shape():
    def __init__(self):
        self.color="Blue"
        self.sides=0
    def area(self):
        return 0

class square(Shape):
    def __init__(self,w,c):
        Shape.__init__(self)
        self.width=w
        self.color=c
    def area(self):
        return self.width**2

class circle(Shape):
    def __init__(self,r,c):
        Shape.__init__(self)
        self.radius=r
        self.color=c
    def area(self):
        return math.pi * (self.radius**2)

sq1= square(5,"BLue")
sq2=square(25,"Red")

c=circle(7,"Green")

print("Sq1",sq1.area())
print("Sq2",sq2.area())

print("Circle",c.area())

