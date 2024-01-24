import tkinter
import tkinter.font as tk_font
window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=tkinter.Label(window, text="이찬서 중3", width=10, height=5, fg="red", relief="solid")
label.pack()

entry=tkinter.Entry(window)
entry.pack()

def 이름(name):
    label.config(text = name)

button = tkinter.Button(window, text="make none", overrelief="solid", width=15, repeatdelay=10, repeatinterval=300, command = (lambda : 이름(" ")))
button.pack()

window.mainloop()