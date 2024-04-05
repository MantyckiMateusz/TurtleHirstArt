from turtle import Turtle, Screen
from random import randint

turtle = Turtle()
turtle.hideturtle()
screen = Screen()
screen.colormode(255)
pos = [(screen.window_width() / -2)+50, (screen.window_height() / -2)+50]
turtle.teleport(*pos)

window_edge = ((screen.window_width() / 2) - 50, (screen.window_height() / 2) - 50)
while pos[1] <= window_edge[1]:
    while pos[0] <= window_edge[0]:
        rand_color = (randint(0,255), randint(0,255), randint(0,255))
        turtle.color(rand_color, rand_color)
        turtle.dot(50)
        pos[0] += 80
        turtle.teleport(*pos)
    pos = [(screen.window_width() / -2)+50, pos[1]+75]
    turtle.teleport(*pos)


screen.exitonclick()

