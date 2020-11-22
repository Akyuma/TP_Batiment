import turtle
from random import *
from turtle import *
speed(10)
screensize(1000,1000)
floar = randint(1,4)
def carre(x,y,width,height,couleur) :
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.goto(x,y)
    for i in range(2):
        turtle.pendown()
        turtle.fd(width)
        turtle.left(90)
        turtle.fd(height)
        turtle.left(90)
        turtle.penup()
    turtle.end_fill()

def sol(x,y,pen):
    x = 0
    y = 0
    x-=20
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pensize(pen)
    turtle.fd(200)
    turtle.pensize(1)
    turtle.penup()


def balcon(x,y,width,height):
    turtle.pensize(3)
    turtle.goto(x,y)
    for i in range(2):
        turtle.pendown()
        width+=5
        turtle.fd(width)
        turtle.left(90)
        turtle.fd(height)
        turtle.left(90)
        turtle.penup()
    for i in range(4):
        turtle.pendown()
        turtle.fd(5)
        turtle.left(90)
        turtle.fd(height)
        turtle.right(90)
        turtle.fd(5)
        turtle.right(90)
        turtle.fd(height)
        turtle.left(90)
        turtle.penup()
    turtle.pensize(1)

def toit(x,y,color):
    turtle.goto(x,y)
    toit=randint(1,2)
    if toit == 1 :
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.right(180)
        turtle.forward(10)
        turtle.right(160)
        turtle.forward(95)
        turtle.right(40)
        turtle.forward(95)
        turtle.left(200)
        turtle.forward(10)
        turtle.right(180)
        turtle.end_fill()
    elif toit == 2:
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.penup()
        turtle.circle(5,180,20)
        turtle.pendown()
        turtle.circle(5,180,20)
        turtle.forward(160)
        turtle.circle(5,180,20)
        turtle.forward(160)
        turtle.right(180)
        turtle.penup()
        turtle.end_fill()

def immeuble() :
    y = 0
    x = 0
    for i in range(floar) :
        immeuble=carre(x,y,160,80,"cyan")
        y = y + 80
    oui = toit(x,y,"Black")
    non = sol(x,y,4)

def porte() :
    porte = randint(1,3)
    if porte == 1 :
        for i in range(1) :
            porte=carre(20,0,30,60,"brown")
            fenetre=carre(65,30,30,30,"white")
            fenetre=carre(110,30,30,30,"white")
    elif porte == 2 :
        for i in range(1) :
            fenetre=carre(20,30,30,30,"White")
            porte=carre(65,0,30,60,"brown")
            fenetre=carre(110,30,30,30,"White")
    elif porte == 3 :
        for i in range(1) :
            fenetre=carre(20,30,30,30,"white")
            fenetre=carre(65,30,30,30,"white")
            porte=carre(110,0,30,60,"brown")


def fenetre() :
    x = 20
    y = 80
    for i in range(1,floar) :
        for i in range(3) :
            fenetre=randint(1,3)
            if fenetre > 1 :
                y+=30
                fene=carre(x,y,30,30,"white")
                y-=30
                x+=45
            elif fenetre == 1:
                fene=carre(x,y,30,60,"white")
                fene=balcon(x,y,30,30)
                x+=45
        y+=80
        x-=135

print(immeuble())
print(porte())
print(fenetre())