import turtle
import math
import random
turtle.speed(0)
phi = 360 / 7
r = 50

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def color_circle(col, rad):
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()
    
def draw_circles(draw_x, draw_y):
    gotoxy(draw_x, draw_y)
    turtle.circle(80)
    gotoxy(draw_x, draw_y + 160)
    color_circle('red', 5)

    for i in range(0, 7):
        phi_rad = phi*i*math.pi/180.0
        gotoxy(draw_x+math.sin(phi_rad)*r, draw_y+math.cos(phi_rad)*r+60)
        color_circle('white', 22)

def pif_paf(pif_x, pif_y, begin):
    for i in range(begin, random.randrange(7, 100)):
        phi_rad = phi*i*math.pi/180.0
        gotoxy(pif_x+math.sin(phi_rad)*r, pif_y+math.cos(phi_rad)*r+60)
        color_circle('brown', 22)
        color_circle('white', 22)

    gotoxy(pif_x+math.sin(phi_rad)*r, pif_y+math.cos(phi_rad)*r+60)
    color_circle('brown', 22)
    
    return i % 7

draw_circles(0, 0)

answer = ""
begin = 0

while answer != 'Нет':
    
    answer = turtle.textinput("Зарядить пистолет?", "Да/Нет")
    
    if answer == 'Да':
        begin = pif_paf(0, 0, begin)
        
        if begin == 0:
            gotoxy(-150, 250)
            turtle.write('Вы проиграли!', font=("Arial", 18, "normal"))
    else:
        pass