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


p = Point(7, 6)
print(p.distanceFromOrigin())
