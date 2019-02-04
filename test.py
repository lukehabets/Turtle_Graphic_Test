import turtle

x = 0

turtle.pencolor('yellow')
turtle.bgcolor('pink')
turtle.speed(0)
turtle.width(5)
turtle.hideturtle()

while(x < 25):
    turtle.forward(x)
    x = x + .1
    turtle.right(15)

while(x < 50):
    turtle.pencolor('blue')
    turtle.forward(x)
    x = x + .1
    turtle.right(15)

while(x<75):
    turtle.pencolor('white')
    turtle.forward(x)
    x = x + .1
    turtle.right(15)
