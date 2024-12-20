import math
from turtle import *

def Heart():

    def hearta(k):
        return 15 * math.sin(k)**3

    def heartb(k):
        return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

    speed(6000)  # Maximum speed
    bgcolor("black")
    penup()  # Start without drawing
    goto(0, 0)  # Move to the center
    pendown()  # Start drawing

    for i in range(60000):  # Reduced for testing
        x = hearta(i / 100) * 20  # Scale and smooth movement
        y = heartb(i / 100) * 20
        goto(x, y)
        color("red")

    done()

    """A Drawing Project With A Friend Whom She Had An Intrested In Turtle Module"""
    """I Might Change The Design"""