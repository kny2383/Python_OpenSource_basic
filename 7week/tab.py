from tkinter import *
from tkinter import ttk
from PIL import ImageTk 

## 2021041059_김나영
window = Tk()
window.iconbitmap('python.ico') # 실행 프로그램 왼쪽 상단에 표시

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text='강아지')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text='고양이')

baseTab.pack(expand=1, fill="both") # 탭을 화면에 표시한다.

photoDog=ImageTk.PhotoImage(file="dog7.gif")
labelDog = Label(tabDog, image = photoDog)
labelDog.pack()

photoCat = ImageTk.PhotoImage(file = "cat5.gif")
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()


window.mainloop()
