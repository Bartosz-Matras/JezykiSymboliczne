#====================================
#             Saper
#      Autor: Bartosz Matras
#====================================


#=================Lib================
import tkinter
import random
from tkinter import messagebox


class mainWindow:

    def __init__(self, master):
        try:
            self.buttonYes.destroy()
            self.buttonNo.destroy()
            self.sure1.destroy()
        except:
            pass

        try:
            self.buttonYes2.destroy()
            self.buttonNo2.destroy()
            self.sure2.destroy()
        except:
            pass


        self.amountOfMines = None
        self.N = None
        self.M = None
        self.master = master
        self.master.configure(bg='grey')
        self.master.geometry('410x200')                # Nie dodacwac tego
        self.master.resizable(0, 0)
        self.master.iconphoto(False, tkinter.PhotoImage(file=r'icon.png'))

        self.buttonPlay = tkinter.Button(self.master, text='Play', width=25, height=4, bg='snow', command=lambda: self.clicked())
        self.buttonQuit = tkinter.Button(self.master, text='Quit', width=25, height=4, bg='snow', command=lambda: self.close_windowYesNo())
        self.labelAuthor = tkinter.Label(self.master, text='Author: Bartosz Matras', width=26, bg='grey')

        self.buttonPlay.grid(row=0, column=0, padx=10, pady=10)
        self.buttonQuit.grid(row=0, column=1, padx=10, pady=10)
        self.labelAuthor.grid(row=1, columnspan=2)

    def clicked(self):
        self.buttonPlay.destroy()
        self.buttonQuit.destroy()
        self.labelAuthor.destroy()

        self.label1 = tkinter.Label(self.master, text='Enter height: ', bg='grey', height=1, width=10, pady=5)
        self.text1 = tkinter.Text(self.master, height=1, width=8, padx=2, pady=5)

        self.label2 = tkinter.Label(self.master, text='Enter width: ', bg='grey', height=1, width=10, pady=5)
        self.text2 = tkinter.Text(self.master, height=1, width=8, padx=2, pady=5)

        self.labelMines = tkinter.Label(self.master, text='Enter amount of mines:', bg='grey', height=1, width=20, pady=10)
        self.textMines = tkinter.Text(self.master, height=1, width=8, padx=2, pady=5)

        self.buttonQuit2 = tkinter.Button(self.master, text='Quit', width=10, height=2, bg='snow', command=lambda: self.close_windowYesNo2())
        self.submit = tkinter.Button(self.master, text='Submit', width=10, heigh=2, bg='snow', command=lambda: self.clicked2())

        self.label1.grid(row=0, column=0, pady=10)
        self.text1.grid(row=0, column=1, pady=10)
        self.label2.grid(row=1, column=0, pady=10)
        self.text2.grid(row=1, column=1, pady=10)
        self.labelMines.grid(row=2, column=0, pady=10)
        self.textMines.grid(row=2, column=1, pady=10)
        self.submit.grid(row=0, column=2, padx=35, pady=10)
        self.buttonQuit2.grid(row=2, column=2, padx=35, pady=10)

    def close_windowYesNo(self):
        self.buttonPlay.destroy()
        self.buttonQuit.destroy()
        self.labelAuthor.destroy()

        self.sure1 = tkinter.Label(self.master, text="Are you sure?", height=1, width=10, pady=10, bg='grey')
        self.buttonYes = tkinter.Button(self.master, text="Yes", width=25, height=4, bg='snow', command=lambda: self.close_window())
        self.buttonNo = tkinter.Button(self.master, text="No", width=25, height=4, bg='snow', command=lambda: self.__init__(self.master))

        self.sure1.grid(row=0, columnspan=2)
        self.buttonYes.grid(row=1, column=0, padx=10, pady=10)
        self.buttonNo.grid(row=1, column=1, padx=10, pady=10)

    def close_windowYesNo2(self):
        self.label1.destroy()
        self.label2.destroy()
        self.text1.destroy()
        self.text2.destroy()
        self.submit.destroy()
        self.buttonQuit2.destroy()
        self.textMines.destroy()
        self.labelMines.destroy()

        self.sure2 = tkinter.Label(self.master, text="Are you sure?", height=1, width=10, pady=10, bg='grey')
        self.buttonYes2 = tkinter.Button(self.master, text="Yes", width=25, height=4, bg='snow',
                                        command=lambda: self.close_window())
        self.buttonNo2 = tkinter.Button(self.master, text="No", width=25, height=4, bg='snow',
                                       command=lambda: self.__init__(self.master))

        self.sure2.grid(row=0, columnspan=2)
        self.buttonYes2.grid(row=1, column=0, padx=10, pady=10)
        self.buttonNo2.grid(row=1, column=1, padx=10, pady=10)

    def close_window(self):
        self.master.destroy()

    def clicked2(self):
        try:
            self.boo1 = False
            self.N = int(self.text1.get("1.0", "end-1c"))
            self.M = int(self.text2.get("1.0", "end-1c"))
            self.amountOfMines = int(self.textMines.get("1.0", "end-1c"))
            if self.M <= 2:
                messagebox.showerror("error", 'Width should be greater than 8')
            elif self.N <= 2:
                messagebox.showerror("error", 'Height should be greater than 8')
            # elif self.N - self.M > 10 or self.M - self.N > 10:
            #     messagebox.showerror("error", 'Too many difference between width and height')
            elif self.amountOfMines <= 0 or self.amountOfMines > self.M * self.N:
                messagebox.showerror("error", 'Incorrect amount of mines')
            elif self.N > 15:
                messagebox.showerror("error", 'Width should be lower than 15')
            elif self.M > 15:
                messagebox.showerror("error", 'Height should be lower than 15')
            else:
                self.boo1 = True

            if self.boo1:
                # self.submit.destroy()
                self.newWindow = tkinter.Toplevel(self.master)
                self.app = Play(self.newWindow, self.N, self.M, self.amountOfMines)

        except ValueError:
            messagebox.showerror("error", 'This is NOT an integer number!')


class Play:
    def __init__(self, master, N, M, amountOfMines):
        self.N = N
        self.M = M
        self.amountOfMines = amountOfMines
        self.time = 0
        self.master = master
        # self.master.geometry('410x200')
        self.master.iconphoto(False, tkinter.PhotoImage(file=r'icon.png'))
        self.frame = tkinter.Frame(self.master)

        #========== Menu ==============================
        # self.myMenu = tkinter.Menu(self.master)
        # self.master.config(menu=self.myMenu)
        # self.newGame = tkinter.Menu(self.myMenu)
        # self.myMenu.add_cascade(label="New Game", menu=self.newGame)
        # self.newGame.add_command(label="New Game", command=self.newGameFun)
        # self.newGame.add_separator()
        # self.newGame.add_command(label="Exit", command=self.exitGame)
        #===============================================

        self.mines = tkinter.Label(self.master, bg='grey', fg='red2', font=('BOLD', 30))
        self.mines.grid(row=0, column=0, padx=35, pady=10)
        self.minesFun()

        # self.start = tkinter.Button(self.master, text='Start', width=15, height=2, bg='snow', command=lambda: self.buttonsFun())
        # self.start.grid(row=0, column=self.M // 2)
        self.newGame = tkinter.Button(self.master, text='New Game', width=15, height=2, command=lambda: self.newGameFun())
        self.newGame.grid(row=0, column=1, padx=30, pady=10)

        self.timer = tkinter.Label(self.master, bg='grey', fg='red2', font=('BOLD', 30))
        self.timer.grid(row=0, column=2, padx=30, pady=30)
        self.clock()

        self.emptyLabel = tkinter.Label(self.master, text=' ')
        self.emptyLabel.grid(row=1, columnspan=self.M)

        self.frame.grid(row=2, columnspan=M, pady=20)

        self.game()


    def clock(self):
        self.time += 1
        self.timer['text'] = '0'*(4 - len(str(self.time))) + str(self.time)
        self.master.after(1000, self.clock)

    def minesFun(self):
        self.mines['text'] = '0'*(4 - len(str(self.amountOfMines))) + str(self.amountOfMines)

    def newGameFun(self):
        self.master.destroy()

    def neighbour(self, tab, x, y):
        self.x = x
        self.y = y
        self.tab = tab
        self.neigh = []

        for i in range(-1,2):
            for j in range(-1,2):
                if not (i == 0 and j == 0):
                    if y + i >= 0 and y + i < self.N:
                        if x + j >= y and x + j < self.M:
                            self.neigh.append((x + j, y + i))
        return self.neigh

    def logic(self):
        self.tab = [[0 for j in range(self.M)] for i in range(self.N)]
        self.minesVar = self.amountOfMines

        while self.minesVar:
            self.x = random.randint(0, self.M - 1)
            self.y = random.randint(0, self.N - 1)

            if self.tab[self.y][self.x] == 0:
                self.tab[self.y][self.x] = 'x'
                self.minesVar -= 1

        for i in range(self.N):
            for j in range(self.M):
                if self.tab[i][j] == 0:
                    self.neighb = self.neighbour(self.tab, j, i)
                    self.minesVar = 0

                    for x, y in self.neighb:
                        if self.tab[y][x] == 'x':
                            self.minesVar += 1

                    self.tab[i][j] = self.minesVar
        return self.tab

    def game(self):
        # =========== Buttons =============================
        buttons = [tkinter.Button(self.frame, height=1, width=2) for i in range(self.N * self.M)]
        self.logic()

        for i in range(self.N):
            for j in range(self.M):
                if j == 0:
                    buttons[i * self.M + j].grid(row=i + 1, column=j, padx=(20, 0))
                elif j == self.M - 1:
                    buttons[i * self.M + j].grid(row=i + 1, column=j, padx=(0, 20))
                else:
                    buttons[i * self.M + j].grid(row=i + 1, column=j)
                    buttons[i * self.M + j].bind('<Button-1>', lambda event, : self.leftButton())
                    buttons[i * self.M + j].bind('<Button-3>', lambda event, p=buttons[i * self.M + j]: self.rightButtom(p, self.iconss()))

    def leftButton(self):
        pass

    def rightButtom(self, button, icon):
        self.button = button
        self.icon = icon

        self.button['image'] = self.icon['flag']

    def iconss(self):
        self.icons = {}

        self.icons['numbers'] = [tkinter.PhotoImage(file='Icons/' + str(i) + '.png') for i in range(1, 9)]
        self.icons['flag'] = tkinter.PhotoImage(file='Icons/a.png')
        self.icons['mine'] = [tkinter.PhotoImage(file='Icons/rock.png'), tkinter.PhotoImage(file='Icons/rockp.png')]

        return self.icons

    # def exitGame(self):
    #     self.master.quit()

    # def buttonsFun(self):
    #     # self.start.destroy()
    #
    #     buttons = [tkinter.Button(self.frame, height=1, width=2) for i in range(self.N * self.M)]
    #
    #     for i in range(self.N):
    #         for j in range(self.M):
    #             buttons[i * self.M + j].grid(row=i+1, column=j)


class SizeError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def main():
    root = tkinter.Tk(className='Saper')

    app = mainWindow(root)

    root.mainloop()


if __name__ == '__main__':

    main()