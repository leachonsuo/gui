import tkinter as tk
import random

class 공피하기게임():
    def __init__(self, window):
        self.window = window
        self.window.title("간단게임")
        self.window.geometry("600x600")
        self.canvas = tk.Canvas(self.window , width=500, height=500, bg='white')
        self.canvas.pack()
        self.player = self.canvas.create_oval(40,40,70,70, fill = 'blue')

    def 먹이생성(self):
        self.먹이들 = []
        for i in range(10):
            x = random.randint(20,480)
            y = random.randint(20,480)
            self.b1 = self.canvas.create_oval(x,y,x+20,y+20 , fill = 'red')
            self.먹이들.append(self.b1)

    def 충돌(self):
        p = self.canvas.coords(self.player)
        for 먹이 in self.먹이들:
            b = self.canvas.coords(먹이)
            if (p[0] <= b[0] <= p[2]) and (p[1] <= b[1] <= p[3]):
                self.canvas.delete( self.먹이들.pop(self.먹이들.index(먹이)))

    def 위로(self, event):
        self.canvas.move(self.player , 0,-10)
        self.충돌()

    def 아래(self, event):
        self.canvas.move(self.player , 0,10)

    def 왼쪽(self, event):
        self.canvas.move(self.player , -10,0)

    def 오른쪽(self, event):
        self.canvas.move(self.player , 10,0)

    def 움직이기(self):
        self.window.bind("<w>", self.위로)
        self.window.bind("<s>", self.아래)
        self.window.bind("<a>", self.왼쪽)
        self.window.bind("<d>", self.오른쪽)

window = tk.Tk()
game = 공피하기게임(window)
game.먹이생성()
game.움직이기()
game.충돌()

window.mainloop()