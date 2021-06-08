import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 300, 300)

f = open("mystery.txt", "r")

for aline in f:
    items = aline.split()
    if items[0] == "UP":
        t.up()
    elif items[0] == "DOWN":
        t.down()
    elif items[0] != "UP" and items[0] != "DOWN":
        t.goto(int(items[0]), int(items[1]))

f.close()
wn.exitonclick()
