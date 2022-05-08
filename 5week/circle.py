import turtle
import random
import math
from tkinter.simpledialog import *

#2021041059_김나영
inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = 0,0,20
radius, angle, radian = 100, 0, 0

turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)	 
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

angle = 360 / len(inStr)

for ch in inStr :

    radian = 3.14 * angle / 180

    tX = radius * math.cos(radian)
    tY = radius * math.sin(radian)
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.goto(tX, tY) 
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

    radius += 5 # 나선형 곡선이 되기 위해 반지름 확대
    angle += 360*2 / len(inStr)

turtle.done()
