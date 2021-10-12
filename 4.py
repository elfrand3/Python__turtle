import turtle

turtle.Screen()
turtle.bgcolor("black")
turtle.title('Animation')

turtle = turtle.Turtle()
turtle.color("yellow")
turtle.speed(0)
turtle.hideturtle()
for i in range(100):
    turtle.circle(i*2)
    turtle._rotate(5)

turtle.done()

