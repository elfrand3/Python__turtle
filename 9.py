from turtle import *

bgcolor('black')
hideturtle()
speed(11)
for i in range(120):
    if i % 2 == 0:
        color('cyan',)
    elif i % 3 == 1:
        color('yellow',)
    elif i % 3 == 2:
        color('green',)
    else :
        color('red')
    forward(i*3)
    left(91)
done()
    