import turtle # turtle 모듈을 사용하기 위해선 import 해야함

num = 0 # 10진수 입력받는 변수 
swidth, sheight = 1000, 500 # 창의 폭과 넓이
curX, curY = 0, 0 # 거북이 현재 위치

if __name__ == "__main__" : # 현재 스크립트 파일이 실행되는 상태를 파악하기 위해 사용

    #2021041059_김나영
    turtle.title('거북이로 2진수 숫자 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50) # 창크기
    turtle.screensize(swidth, sheight)
    turtle.penup() # 펜 이동시 라인을 그리지 않는다.
    turtle.left(90) # 터틀을 90도 만큼 왼쪽으로 방향 전환
    
    num = int(input("숫자를 입력하세요 : "))
    binary = bin(num) # 2진수 문자열로 변환
    curX = swidth / 2 # 거북이의 초기 위치를 윈도창의 오른쪽 끝으로 설정
    curY = 0
    print(binary)
    print(len(binary))

    for i in range(len(binary) - 2) : # 변환한 2진수의 개수만큼 반복
        turtle.goto(curX, curY)
        if num & 1 : # 맨 하위 비트가 1인지 확인하고 맞다면 빨간색으로 설정
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue') # 아니면 파란색으로 설정
            turtle.turtlesize(1)
        turtle.stamp() # 거북이 도장찍기
        curX -= 50 # 거북이 이동
        num >>= 1 # 오른쪽 비트는 앞에서 사용했으므로 없애기
        
turtle.done()

 
