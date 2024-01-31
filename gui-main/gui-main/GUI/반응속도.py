import tkinter
import tkinter.font as tk_font
import random
import math
import time


window=tkinter.Tk()
window.title("반응속도 테스트")
window.geometry("640x400+100+100")
window.resizable(False, False)


def 시작(button, button1):
    a = random.randrange(1,10)
    button.pack_forget()
    yet.pack()
    time.sleep(a)
    global start1
    start1 = time.time()
    math.factorial(100000)
    button1.pack_forget()
    now.pack()
    
def 끝():
    end = time.time()
    c = f"{end*1000 - start1*1000:.5f} ms"
    label.config(text=str(c))
    print(c)
    
def 실패(button):
    button.pack()

font = tk_font.Font(family = "맑은 고딕", size=10)

label = tkinter.Label(window, text='', width=30, height=1, fg="black", relief="solid" , font = font)
label.pack()

start = tkinter.Button(window, text="시작", width=100, height=10, repeatdelay=10000,
                        repeatinterval=300, command =lambda : 시작(start, yet))
start.pack()

yet = tkinter.Button(window, text="아직", overrelief="solid", width=100, height=10, repeatdelay=10000, repeatinterval=300, command = lambda : 실패(failed))

failed = tkinter.Button(window, text="실패", overrelief="solid", width=100, height=10, repeatdelay=10000, repeatinterval=300)

now = tkinter.Button(window, text="지금", overrelief="solid", width=100, height=10, repeatdelay=10000, repeatinterval=300, command = lambda : 끝())

window.mainloop()