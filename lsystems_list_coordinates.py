import turtle

def drawLsystem(aTurtle, instructions, angle, distance):
    saveInfoList = []
    for cmd in instructions:
        if cmd == "F":
            aTurtle.forward(distance)
        elif cmd == "B":
            aTurtle.backward(distance)
        elif cmd == "+":
            aTurtle.right(angle)
        elif cmd == "-":
            aTurtle.left(angle)
        elif cmd == "[":
            saveInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
            print(saveInfoList)
        elif cmd == "]":
            newInfo = saveInfoList.pop()
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1], newInfo[2])

t = turtle.Turtle()
t.speed(25)
inst = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF[-FFFFFFFFFFFFFFFF[-FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFFFFFFFFFFFFFF[-FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X"
t.setposition(0, -200)
t.left(90)
drawLsystem(t, inst, 30, 2)
            
