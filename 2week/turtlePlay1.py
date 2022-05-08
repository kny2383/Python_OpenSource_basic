import turtle #turtle 모듈을 사용하려면 프로그램 시작 전에 반드시 import 해야힘
import random #아래에서 random() 함수를 사용하기 때문에 import 해야함


##함수 선언 부분##

def turtleMoving(x, y):

    ##전역변수 선언 부분##
    global r, g, b 

    r = random.random() #색상 랜덤 지정

    g = random.random()

    b = random.random()


    #2021041059_김나영
    size = random.randrange(1, 6) #크기는 1부터 5까지

    angle = random.randrange(0, 361) #0부터 360도 까지


    turtle.shapesize(size)

    turtle.color(r, g, b) #현재 색을 설정함

    turtle.right(angle) #turtle을 오른쪽으로 angle도 회전시킴


    turtle.stamp() #거북이 도장찍기


    turtle.goto(x, y) #거북이 이동


r, g, b = 0.0, 0.0, 0.0 #변수 초기값


##메인(main) 코드 부분 ##
turtle.title("거북이 도장찍기") #윈도우창의 제목 설정하기

turtle.shape("turtle") # 매개변수: name, 주어진 name의 모양으로 거북이 모양을 설정하거나, 이름이 없으면 현재 모양의 이름을 반환한다.

turtle.onscreenclick(turtleMoving, 3) #turtle.onscreenclick(함수명, 번호) -> 3번은 마우스 오른쪽 버튼 지정
 

turtle.done() #turtle 그래픽 화면을 붙잡아두는 역할
