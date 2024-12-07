import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()

pen.speed(6)
pen.pensize(6)

pen.hideturtle()


pen.color("red", "white")

pen.begin_fill()

def lift():
    pen.up()
    pen.goto(0, 180)
    pen.down()

def top_right():
    pen.left(315)
    pen.forward(245)

def bottom_right():
    pen.left(270)
    pen.forward(245)

def bottom_left():
    pen.left(270)
    pen.forward(245)

def top_left():
    pen.left(270)
    pen.forward(245)
    pen.end_fill()
    screen.exitonclick()

lift()
top_right()
bottom_right()
bottom_left()
top_left()

"""Finished Rhombus Drawing"""