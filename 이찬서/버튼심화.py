# (lambda x,y: x + y)

import tkinter
import tkinter.font as tk_font

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

label = tkinter.Label(window, text = "나오는 값")
label.pack()

button = tkinter.Button(window, text = "람다사용", overrelief='solid', width=15, command = (lambda : 이름("찬서")))
button.pack()

window.mainloop()