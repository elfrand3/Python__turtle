import turtle
loodwindow = turtle.Screen()
turtle.speed(2)
for x in range(100):
    turtle.circle(5*x)
    turtle.circle(-5*x)
    turtle.left(x)

turtle.exitonclick()