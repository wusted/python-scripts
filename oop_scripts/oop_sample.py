
class Phone:
    """ This is a class to generate Phones with different color and size """

    def __init__(self, col, siz):
        self.color = col
        self.size = siz

    def getcolor(self):
        return self.color

    def getsize(self):
        return self.size

    def __str__(self):
        return "My Phone color is " + str(self.color) + ", with size " + str(self.size)

object1 = Phone("red", "10cm")
print(object1)

object2 = Phone("black", "12cm")
print(object2)

for i in range(2):
    choose_color = str(input("Please choose a color for your Phone: ")) 
    choose_size = str(input("Please choose a size for your Phone: "))
    object3 = Phone(choose_color, choose_size)
    print(object3)
