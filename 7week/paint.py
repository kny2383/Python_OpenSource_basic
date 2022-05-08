# askcolor()와 askinteger()함수를 사용하기 위한 모듈 임포트
from tkinter import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *

## 함수 선언 ##
## 2021041059_김나영

def mouseClick(event) : # 마우스를 클릭하는 순간에 시작점 전역변수 x1,y1의 값을 설정한다.
    global x1,y1,x2,y2 
    x1 = event.x
    y1= event.y

def mouseDrop(event) : # 마우스를 드롭하는 순간에 끝점 전역변수 x2,y2의 값을 설정한다.
    global x1,y1,x2,y2,penWidth, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1,y1,x2,y2, width = penWidth, fill = penColor) # 시작점과 끝점에 선을 긋는다.

def getColor() :
    global penColor
    color = askcolor() # 색상 선택하는 askcolor() 함
    penColor = color[1] # color[1]인 이유: 반환 값이 튜플((r,g,b),#rrggbb)형태 여서

def getWidth() :
    global penWidth
    penWidth = askinteger("선 두께", "선 두께(1~10)를 입력하세요", minvalue = 1, maxvalue = 10)

## 전역 변수 선언 ##
window = None
canvas = None
x1,y1,x2,y2 = None, None, None, None 
penColor = 'black'
penWidth = 5

## 메인 코드 ##
if __name__ == "__main__" : 
    window = Tk()
    window.title("그림판 비슷한 프로그램")
    canvas = Canvas(window, height = 300, width = 300)
    canvas.bind("<Button-1>", mouseClick) # 마우스 왼쪽 버튼 클릭시 mouseClick() 함수 실행
    canvas.bind("<ButtonRelease-1>", mouseDrop) # 드롭하면 mouseDrop() 함수 실행
    canvas.pack()

    mainMenu = Menu(window) 
    window.config(menu = mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "설정", menu = fileMenu)
    fileMenu.add_command(label = " 선 색상 선택", command = getColor)
    fileMenu.add_separator()
    fileMenu.add_command(label= "선 두께 설정", command = getWidth)

    window.mainloop()
    
