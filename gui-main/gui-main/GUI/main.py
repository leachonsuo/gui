import tkinter
import tkinter.font as tk_font
window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

font = tk_font.Font(family = "맑은 고딕", size=20)
label=tkinter.Label(window, text="파이썬", width=10, height=5, fg="red", relief="solid" , font = font)
label.pack()

#버튼

c = 0

def up():
    global c
    c += 1
    label.config(text=str(c))

def down():
    global c
    c -= 1
    label.config(text=str(c))

button = tkinter.Button(window, text="+", overrelief="solid", width=15, repeatdelay=10, repeatinterval=300, command=up)
button2 = tkinter.Button(window, text="-", overrelief="solid", width=15, repeatdelay=10, repeatinterval=300, command=down)
button.pack()
button2.pack()

window.mainloop()