import tkinter
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tk_font
import face
import cat

window=tkinter.Tk()
window.title("인식기능")
window.geometry("640x400+100+100")
window.resizable(False, False)

font = tk_font.Font(family = "맑은 고딕", size=20)

face = tkinter.Button(window, text="얼굴", font = font, overrelief="solid", width=15, repeatdelay=10, repeatinterval=300, command = face.얼굴인식)
face.pack()

cat = tkinter.Button(window, text="고양이", font = font, overrelief="solid", width=15, repeatdelay=10, repeatinterval=300, command = cat.고양이인식)
cat.pack()

body = tkinter.Button(window, text="몸", font = font, overrelief="solid", width=15, repeatdelay=10, repeatinterval=300)
body.pack()

hand = tkinter.Button(window, text="손", font = font, overrelief="solid", width=15, repeatdelay=10, repeatinterval=300)
hand.pack()

window.mainloop()