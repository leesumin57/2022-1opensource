import turtle
import math
import random

## 2021041039 이수민 ##

t1, t2, t3 = [None] * 3
t1x, t1y, t2x, t2y, t3x, t3y = [0] * 6
swidth, sheight = 300, 300

if __name__ == "__main__" :
    turtle.title('거북이 서로 만나게 하기')
    turtle.setup(width = swidth + 50, height = sheight +50)
    turtle.screensize(swidth, sheight)

    t1 = turtle.Turtle('turtle'); t1.color('yellow'); t1.penup()
    t2 = turtle.Turtle('turtle'); t2.color('purple'); t2.penup()
    t3 = turtle.Turtle('turtle'); t3.color('green'); t3.penup()

    t1.goto(-100, -100); t2.goto(0,0); t3.goto(100,100)

    while True :
        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t1.left(angle); t1.forward(dist)
        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t2.left(angle); t2.forward(dist)
        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t3.left(angle); t3.forward(dist)

        t1x = t1.xcor(); t1y = t1.ycor()
        t2x = t2.xcor(); t2y = t2.ycor()
        t3x = t3.xcor(); t3y = t3.ycor()

        if math.sqrt(((t1x - t2x) * (t1x - t2x)) + ((t1y - t2y) * (t1 - t2y))) <= 20 or \
          math.sqrt(((t1x - t3x) * (t1x - t3x)) + ((t1y - t3y) * (t1 - t3y))) <= 20 or \
          math.sqrt(((t2x - t3x) * (t2x - t3x)) + ((t2y - t3y) * (t2 - t3y))) <= 20 :
          t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
          break

turtle.done()

# TypeError: unsupported operand type(s) for -: 'Turtle' and 'float'
