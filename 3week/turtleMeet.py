import turtle # turtle 모듈을 사용하기 위해 선언
import math # math 모듈을 사용하기 위해 선언
import random # random 모듈을 사용하기 위해 선언

#2021041059 김나영

## 전역 변수 선언 ##
t1, t2, t3 = [None] * 3 # None을 3번 선언한 것과 동일
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6 # 0을 6번 선언한 것과 동일
swidth, sheight = 300, 300 # 윈도창 크기

## 메인 코드 ##
if __name__ == "__main__" : 
    turtle.title('거북이 서로 만나게 하기')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    t1 = turtle.Turtle('turtle'); t1.color('red'); t1.penup() 
    t2 = turtle.Turtle('turtle'); t2.color('green'); t2.penup()
    t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.penup()

    t1.goto(-100, -100); t2.goto(0,0); t3.goto(100, 100) # 거북이 초기 위치 다르게 하기
    t1.speed(10); t2.speed(10); t3.speed(10) # 거북이의 속도를 빠르게 하기

    # 거북이를 만날 때까지 무한 반복
    while True :
        angle = random.randrange(0, 360) # 각도
        dist = random.randrange(1, 50) # 거리
        t1.left(angle); t1.forward(dist)

        angle = random.randrange(0, 360) # 각도
        dist = random.randrange(1, 50) # 거리
        t2.left(angle); t2.forward(dist)

        angle = random.randrange(0, 360) # 각도
        dist = random.randrange(1, 50) # 거리
        t3.left(angle); t3.forward(dist)

        #거북이의 현재 위치
        # 거북이의 x좌표와 y좌표를 각각의 변수에 저장
        t1X = t1.xcor(); t1Y = t1.ycor() 
        t2X = t2.xcor(); t2Y = t2.ycor()
        t3X = t3.xcor(); t3Y = t3.ycor()

        #거북이끼리의 거리가 20미만이면 만난 것으로 처리
        if math.sqrt(((t1X - t2X) * (t1X- t2X)) + ((t1Y- t2Y) * (t1Y- t2Y))) <= 20 or \
           math.sqrt(((t1X - t3X) * (t1X- t3X)) + ((t1Y- t3Y) * (t1Y- t3Y))) <= 20 or \
           math.sqrt(((t2X - t3X) * (t2X- t3X)) + ((t2Y- t3Y) * (t2Y- t3Y))) <= 20 :
            t1. turtlesize(3); t2.turtlesize(3); t3.turtlesize(3) # 거북이끼리 만나면 거북이의 크기를 세 배로 확대
            break

turtle.done()
           
           


        
