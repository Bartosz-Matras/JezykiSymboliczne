import tkinter
import random
from tkinter import messagebox
import time


class Play:
    def __init__(self, master, N, M, amountOfMines):
        self.__N = N
        self.__M = M
        self.__amountOfMines = amountOfMines
        self.__amountOfHitMines = 0
        self.__flagsLeft = self.__amountOfMines
        self.__time = 0
        self.__master = master
        self.__z = str()
        self.__master.config(bg='grey71')
        self.__master.iconphoto(False, tkinter.PhotoImage(file=r'Img/icon.png'))
        self.frame = tkinter.Frame(self.__master)
        self.frame.config(bg='grey71')
        self.__master.bind("<Key>", self.funXyzzy)

        self.mines = tkinter.Label(self.__master, bg='grey33', fg='red2', font=('BOLD', 30))
        self.mines.grid(row=0, column=0, padx=35, pady=10)
        self.minesFun()

        self.newGame = tkinter.Button(self.__master, text='New Game', width=15, height=2, command=lambda: self.newGameFun())
        self.newGame.grid(row=0, column=1, padx=30, pady=10)

        self.timer = tkinter.Label(self.__master, bg='grey33', fg='red2', font=('BOLD', 30))
        self.timer.grid(row=0, column=2, padx=30, pady=30)
        self.clock()

        self.emptyLabel = tkinter.Label(self.__master, text=' ')
        self.emptyLabel.grid(row=1, columnspan=self.__M)

        self.frame.grid(row=2, columnspan=M, pady=20)

        self.game()

    def funXyzzy(self, event):
        lista = []
        lista.append(event.char)

        for x in lista:
            self.__z += str(x)

        if self.__z == 'xyzzy':
            for i in range(self.__N):
                for j in range(self.__M):
                    if self.tab[i][j] == 'x':
                        self.buttons[i * self.__M + j]['background'] = 'salmon1'

    def clock(self):
        self.__time += 1
        self.timer['text'] = '0'*(4 - len(str(self.__time))) + str(self.__time)
        self.__master.after(1000, self.clock)

    def minesFun(self):
        self.mines['text'] = '0'*(4 - len(str(self.__flagsLeft))) + str(self.__flagsLeft)

    def newGameFun(self):
        self.__master.destroy()

    def neighbour(self, tab, x, y):
        neigh = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    if 0 <= y + i < self.__N:
                        if 0 <= x + j < self.__M:
                            neigh.append((x + j, y + i))
        return neigh

    def logic(self):
        self.tab = [[0 for j in range(self.__M)] for i in range(self.__N)]
        minesVar = self.__amountOfMines

        while minesVar:
            x = random.randint(0, self.__M - 1)
            y = random.randint(0, self.__N - 1)

            if self.tab[y][x] == 0:
                self.tab[y][x] = 'x'
                minesVar -= 1

        for i in range(self.__N):
            for j in range(self.__M):
                if self.tab[i][j] == 0:
                    neighb = self.neighbour(self.tab, j, i)
                    minesVar = 0

                    for x, y in neighb:
                        if self.tab[y][x] == 'x':
                            minesVar += 1

                    self.tab[i][j] = minesVar
        return self.tab

    def game(self):
        # =========== Buttons =============================
        self.buttons = [tkinter.Button(self.frame, heigh=-1, width=-2) for i in range(self.__N * self.__M)]
        self.logic()
        self.icon = self.iconss()

        for i in range(self.__N):
            for j in range(self.__M):
                self.setButtons(j, i)
                self.buttons[i * self.__M + j].bind('<Button-1>', lambda event, p=self.buttons[i * self.__M + j]: self.leftButton(p, self.tab, self.icon))
                self.buttons[i * self.__M + j].bind('<Button-3>', lambda event, p=self.buttons[i * self.__M + j]: self.rightButtom(p, self.icon))



    def updateField(self, indx, field, icons):
        self.buttons[indx].configure(state='disabled', border=2, highlightbackground='yellow')
        self.buttons[indx].config(bg='grey82')
        self.buttons[indx].unbind('<Button-1>')
        self.buttons[indx].unbind('<Button-3>')
        if field != 0:
            self.buttons[indx] = tkinter.Label(self.frame, image=icons['numbers'][field - 1])
            self.setButtons(indx % self.__M, indx // self.__M)
        else:
            self.neig = self.neighbour(self.tab, indx % self.__M, indx // self.__M)

            for x, y in self.neig:
                if isinstance(self.buttons[y*self.__M + x], tkinter.Button) and self.buttons[y*self.__M + x]['state'] != 'disabled':
                    self.updateField(y*self.__M + x, self.tab[y][x], icons)

    def endGame(self, indx, field, icons):
        for i in range(self.__N):
            for j in range(self.__M):
                if isinstance(self.buttons[i*self.__M + j], tkinter.Button) and self.buttons[i*self.__M + j]['state'] != 'disabled':
                    self.buttons[i*self.__M + j]['state'] = 'disabled'
                    self.buttons[i*self.__M + j].unbind('<Button-1>')
                    self.buttons[i*self.__M + j].unbind('<Button-3>')
                    if self.tab[i][j] == 'x':
                        if self.tab[i][j] == indx:
                            self.buttons[i * self.__M + j] = tkinter.Label(self.frame, image=icons['mine'][1])
                            self.setButtons(j, i)
                        else:
                            self.buttons[i*self.__M + j] = tkinter.Label(self.frame, image=icons['mine'][0])
                            self.setButtons(j, i)
        messagebox.showinfo("Game Over", "You loose")


    def leftButton(self, button, tab, icons):
        indx = self.buttons.index(button)
        field = tab[indx//self.__M][indx % self.__M]
        if field == 'x':
            self.endGame(indx, field, icons)
        else:
            self.updateField(indx, field, icons)

    def rightButtom(self, button, icon):
        indx = self.buttons.index(button)
        field = self.tab[indx // self.__M][indx % self.__M]

        if button.cget('image'):
            button.bind("<Button-1>", lambda event, p=button : self.leftButton(p, self.tab, self.icon))
            button['image'] = ''
            self.__flagsLeft += 1
        else:
            button.unbind("<Button-1>")
            if self.__flagsLeft <= 0:
                messagebox.showinfo("Info", "Too many flags")
            else:
                button['image'] = icon['flag']
                self.__flagsLeft -= 1
                if field == 'x':
                    self.__amountOfHitMines += 1
                    if self.__amountOfHitMines == self.__amountOfMines:
                        messagebox.showinfo("Win", "You Win")
                        time.sleep(2)
                        self.__master.destroy()
        try:
            self.minesFun()
        except:
            pass

    def setButtons(self, x, y):
        if x == 0:
            self.buttons[y*self.__M + x].grid(row=y+1, column=x, padx=(20, 0))
        else:
            self.buttons[y*self.__M + x].grid(row=y+1, column=x)

    def iconss(self):
        self.icons = {}

        self.icons['numbers'] = [tkinter.PhotoImage(file='Img/' + str(i) + '.png') for i in range(1, 9)]
        self.icons['flag'] = tkinter.PhotoImage(file='Img/flag1.png')
        self.icons['mine'] = [tkinter.PhotoImage(file='Img/bomb.png'), tkinter.PhotoImage(file='Img/bombr.png')]

        return self.icons
