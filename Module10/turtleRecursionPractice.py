# Name: Ryan Christopher
# Pawprint: rdcb2f
# Challenge: Turtle Recursion Practice
# Module 10

import random
from turtle import Turtle

def turtleRecursion(turtle, angle, quantity, delta, radius):
    turtle.left(10)
    
    for x in range(quantity):
        turtle.color("blue")
        turtle.forward(delta)
        turtle.right(angle)
        turtle.forward(delta)
        turtle.right(angle*2)
        turtle.color("red")
        turtle.forward(delta)
        turtle.right(angle)
        turtle.forward(delta)
        turtle.right(angle*2)
        turtle.left(angle+30)

    delta += 5

    if (delta < radius):
        turtleRecursion(turtle, angle, quantity, delta, radius)

def main():
    ANIMATION_SPEED = 0
    mainTurtle = Turtle()
    mainTurtle.speed(ANIMATION_SPEED)
    turtleRecursion(mainTurtle, 60, 6, 10, 200)

main()