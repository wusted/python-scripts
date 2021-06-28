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

    def __init__(self, initP, initW, initH):

        self.location = initP
        self.width = initW
        self.height = initH

    def getWidht(self):
        return self.width

    def getHeight(self):
        return self.height

    def __str__(self):
        return "Width=" + str(self.width) + ", Height=" + str(self.height)

    def area(self):
        return self.width * self.height

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
print(r)
print(r.area())
