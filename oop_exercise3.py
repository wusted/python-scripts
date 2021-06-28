## Create a Rectangle at a Point specified

class Point:
    
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

class Rectangle:
    """ Rectangle class using Point, width and height. """

    def __init__(self, initP, initW, initL):

        self.location = initP
        self.width = initW
        self.length = initL

    def getWidht(self):
        return self.width

    def getLength(self):
        return self.length

    def __str__(self):
        return "Rectangle's " + "Width=" + str(self.width) + ", Length=" + str(self.length)

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width * 2) + (self.length * 2)

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
print(r)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
