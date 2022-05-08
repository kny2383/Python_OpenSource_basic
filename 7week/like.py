from tkinter import *
from PIL import ImageTk 
## 2021041059_김나영
def myFunc() : # 선택한 라디오 버튼이 이미지를 바꾸도록 하는 함수
    if var.get () == 1 :
        labelImage.configure(image = photo1)
    elif var.get() == 2 :
        labelImage.configure(image = photo2)
    else :
        labelImage.configure(image = photo3)

var, labelImage = 0, None
photo1, photo2, photo3 = [None] * 3

if __name__ == "__main__" :
    window = Tk() #tkinter는 Tk interface의 약어. Tk는 Tcl/Tk라는 전통적인 GUI 인터페이스 윈도, 리눅스, 맥 등에서 모두 동일한 코드로 사용 가능
    window.geometry("400x400") # 윈도창의 크기 설
    window.title("애완동물 선택하기")
    labelText = Label(window,text = "좋아하는 동물 투표 ", fg = "blue", font = ("궁서체",20))

    var = IntVar() #정수 변수로 만드는 함수
    rb1 = Radiobutton(window, text = "강아지", variable = var, value = 1)
    rb2 = Radiobutton(window, text = "고양이", variable = var, value = 2)
    rb3 = Radiobutton(window, text = "토끼", variable = var, value = 3)
    buttonOk = Button(window, text = "사진 보기", command = myFunc) #Button() 함수를 실행하면 마우스로 클릭하면 눌리는 효과와 함께 지정한 작업 실행

    photo1 = ImageTk.PhotoImage(file = "dog7.gif") # PhotoImage()는 이미지 넣는 함수이고 GIF 파일만 지원한다.
    photo2 = ImageTk.PhotoImage(file = "cat5.gif")
    photo3 = ImageTk.PhotoImage(file = "rabbit.gif")

    labelImage = Label(window, width = 200, height = 200, bg = "yellow", image = None)

    labelText.pack(padx =5, pady = 5) # pack() 함수로 화면에 표시
    rb1.pack(padx = 5, pady = 5)
    rb2.pack(padx = 5, pady = 5)
    rb3.pack(padx = 5, pady = 5)
    buttonOk.pack(padx = 5, pady = 5)
    labelImage.pack(padx = 5, pady = 5)

    window.mainloop()
