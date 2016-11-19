import turtle
import random

turtle.speed(0)
turtle.circle(20)

answer = ""
while answer != 'Нет':
    answer = turtle.textinput("Нарисовать окружность", "Да/Нет")
    if answer == 'Да':
        turtle.penup()
        turtle.goto(random.randrange(-300, 300), random.randrange(-300, 300))
        turtle.pendown()
        turtle.fillcolor(random.random(), random.random(), random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1, 100))
        turtle.end_fill()
    else:
        pass