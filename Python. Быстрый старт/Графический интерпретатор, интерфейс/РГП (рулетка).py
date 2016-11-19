import turtle
import math

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def color_circle(col, rad):
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()

turtle.speed(0)
gotoxy(0, 0)
turtle.circle(80)
gotoxy(0, 160)
color_circle('red', 5)


phi = 360 / 7
r = 50

for i in range(0, 7):
    phi_rad = phi*i*math.pi/180.0
    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r+60)
    turtle.circle(22)

gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r+60)
color_circle('brown', 22)