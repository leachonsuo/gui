import tkinter
import tkinter.font as tk_font
import random
import math
import time

start = time.time()
math.factorial(100000)
end = time.time()

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)


def 시작(button):
    button.pack_forget()


font = tk_font.Font(family = "맑은 고딕", size=20)

start = tkinter.Button(window, text="시작", width=100, height=10, repeatdelay=10000,
                        repeatinterval=300, command =lambda : 시작(start))
start.pack()

yet = tkinter.Button(window, text="아직", overrelief="solid", width=100, height=10, repeatdelay=10000, repeatinterval=300)

now = tkinter.Button(window, text="지금", overrelief="solid", width=100, height=10, repeatdelay=10000, repeatinterval=300)

window.mainloop()