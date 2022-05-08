import turtle # turtle 모듈을 사용하기 위해 선언
# 2021041059 김나영

## 전역 변수 선언 ##
i, k = 0, 0 # 반복문 변수 초기화
tX,tY = 0, 0 # 거북이 위치 저장 변수 초기화
swidth, sheight = 800, 450 # 윈도창 크기

## 메인 코드 ##
if __name__ == "__main__" :
    turtle.title('거북이로 구구단 출력하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50) # 윈도창 크기 조정
    turtle.screensize(swidth, sheight)
    turtle.penup() #penup() 거북이가 이동할 때 선을 그리지 않도록 한다
    tX, tY = -500, 250 # 거북이 위치
    turtle.goto(tX, tY) # 거북이 이동

    for i in range(1, 10) :
        for k in range(2, 10) :
            turtle.goto(tX + 80 * k, tY - 40 * i) 
            gugudan = str(k) + 'x' + str(i) + ' = ' + str(k*i) # 구구단 
            turtle.write(gugudan, font = ('Arial', 12, 'bold')) # 출력
            
turtle.done()
