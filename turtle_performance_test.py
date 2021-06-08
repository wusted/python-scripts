#!/bin/python3

import turtle

turtle = turtle.Turtle()

turtle.hideturtle()
s = int(input("Type the speed in number format:  "))
turtle.speed(s)

for i in range(350):
	turtle.forward(i)
	turtle.right(98)


