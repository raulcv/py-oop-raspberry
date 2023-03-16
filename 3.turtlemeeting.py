from turtle import Turtle
from random import randint

laura = Turtle()
raulcv = Turtle()

print("Laura and RAULCV turtles have a meeting")

laura.color('red')
laura.shape('turtle')
laura.left(180)
laura.penup()
laura.speed(3)
laura.goto(160, 100)
laura.pendown()

raulcv.color('purple')
raulcv.shape('turtle')
raulcv.penup()
raulcv.speed(1)
raulcv.goto(-160,100)
raulcv.pendown()

for movement in range(50):
    laura.forward(randint(1,5))
    raulcv.forward(randint(1,5))

input("Press Enter to close the program.")