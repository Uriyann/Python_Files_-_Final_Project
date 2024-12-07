import turtle

screen = turtle.Screen()
screen.bgcolor("black")

p = turtle.Turtle()
p.color("white")
p.pensize(5)
p.speed(4)

p.hideturtle()
p.begin_fill()

def front_hull():

    p.forward(100)
    p.circle(110, 90)
    p.left(90)
    p.forward(300)

def top_flag():
    p.right(90)
    p.forward(150)
    p.right(120)
    p.forward(100)
    p.right(150)
    p.forward(87)

def rear_hull():
    p.left(90)
    p.forward(100)
    p.right(90)
    p.forward(200)
    p.left(90)
    p.circle(110, 90)
    p.forward(200)

front_hull()
top_flag()
rear_hull()

p.end_fill()

screen.exitonclick()

"""Ordinary Python Project With Boat Drawing"""