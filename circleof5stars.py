import turtle

def drawStar(turtle, sides, size, angle):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(angle)
    turtle.penup()
    turtle.forward(350)
    turtle.pendown()

def drawStars(stars, turtles):
    for i in range(stars):
        turtles.right(144)
        drawStar(jean, 5, 100, -144)
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")

jean = turtle.Turtle()
jean.color("pink")
jean.pensize(3)

jean.penup()
jean.backward(-125)
jean.pendown()

drawStars(5, jean)
wn.exitonclick()