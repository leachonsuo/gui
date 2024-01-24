import tkinter
from math import *

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x480+100+100")
window.resizable(False, False)

entry=tkinter.Entry(window)
entry.pack()

entry1=tkinter.Entry(window)
entry1.pack()

label=tkinter.Label(window)
label.pack()
#버튼 기능
def 가져오기():
    s = entry.get() # 가져오는 부분
    s1 = entry1.get()
    answer = int(s) + int(s1)
    label.config(text = str(answer)) # 라벨에 표시


button = tkinter.Button(window, text = "값", command=가져오기)
button.pack()

window.mainloop()