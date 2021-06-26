import math

class Point:
    """Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y **2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


def distance(point1, point2):
    xdiff = point2.getx() - point1.getx()
    ydiff = point2.gety() - point1.gety()

    dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
    return dist

z = Point(7, 6)
print(z.distanceFromOrigin())

p = Point(4, 3)
q = Point(0, 0)
print(distance(p, q))

print(z)
