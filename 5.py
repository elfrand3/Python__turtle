import turtle
import random

a=turtle.Turtle()

x=1

while x<400:
    a.speed(10)
    b=turtle.Screen()
    b.bgcolor("black")
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.colormode(255)
    a.pencolor(r,g,b)
    a.pensize(1)
    a.forward(10+x)
    a.right(90.99)
    x=x+1

turtle.done()