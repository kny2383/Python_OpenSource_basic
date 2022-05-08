import turtle 
import random

## 전역 변수 선언 ##

#2021041059 김나영

aTurtle, tX, tY,tSize = [None] * 4 # 거북이 크기
bTurtle = [] # 정렬 전 거북이
swidth, sheight = 800, 450 # 윈도창 크기

## 메인 함수 구현 ##

if __name__ == "__main__" :

    turtle.title('거북이 선 긋기')
    turtle.shape('turtle')
    turtle.setup(width=swidth + 50, height = sheight + 50) # 윈도창 크기 조정
    turtle.screensize(swidth, sheight)

    for i in range(0,5) : # 거북이 5마리 생성
        aTurtle = turtle.Turtle('turtle') 
        tX = random.randrange(-swidth / 2, swidth / 2) # 거북이 크기 
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random() # 거북이 색상
        g = random.random()
        b = random.random()
        tSize = random.randrange(1,100)/10 # 거북이의 크기 랜덤 설정
        bTurtle.append([aTurtle, tX, tY, r, g, b, tSize]) # 거북이 리스트 생성

    ## tSize를 key로 정렬
    sortedTurtles = sorted(bTurtle, key= lambda turtles : turtles[6])

    for index, tList in enumerate(sortedTurtles[0:]) :
        aTurtle = tList[0]
        aTurtle.color((tList[3],tList[4],tList[5]))
        aTurtle.turtlesize(tList[6])
        tAngle=random.randint(0,360) # 거북이의 각도 랜덤하게 설정
        aTurtle.setheading(tAngle)
        aTurtle.penup()
        if index == 0 :
            aTurtle.goto(tList[1],tList[2])
            continue
        aTurtle.goto(sortedTurtles[index-1][1], sortedTurtles[index-1][2])
        aTurtle.pendown()
        aTurtle.goto(tList[1],tList[2])
    turtle.done()
        
    
