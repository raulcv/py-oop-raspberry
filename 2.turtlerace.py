from turtle import Turtle
from random import randint

laura = Turtle()
rick = Turtle()
lauren = Turtle()
raulcv = Turtle()

print("I created 4 turtles")

laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160,100)
laura.pendown()

rick.color('green')
rick.shape('turtle')
rick.penup()
rick.goto(-160,70)
rick.pendown()


lauren.color('blue')
lauren.shape('turtle')
lauren.penup()
lauren.goto(-160,40)
lauren.pendown()

raulcv.color('purple')
raulcv.shape('turtle')
raulcv.penup()
raulcv.goto(-160,10)
raulcv.pendown()

for movement in range(100):
    laura.forward(randint(1,5))
    rick.forward(randint(1,5))
    lauren.forward(randint(1,5))
    raulcv.forward(randint(1,5))
input("Press Enter to close")