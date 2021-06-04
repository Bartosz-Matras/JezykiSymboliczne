#====================================
#             Saper
#      Autor: Bartosz Matras
#====================================


#=================Lib================
import tkinter
import game
import random
from tkinter import messagebox
import time


class MainWindow:

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

        self.__amountOfMines = None
        self.__N = None
        self.__M = None
        self.__boo1 = None
        self.master = master
        self.master.configure(bg='grey')
        self.master.geometry('410x200')
        self.master.resizable(0, 0)
        self.master.iconphoto(False, tkinter.PhotoImage(file=r'Img/icon.png'))

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
            self.__boo1 = False
            self.__N = int(self.text1.get("1.0", "end-1c"))
            self.__M = int(self.text2.get("1.0", "end-1c"))
            self.__amountOfMines = int(self.textMines.get("1.0", "end-1c"))
            if self.__M <= 2:
                messagebox.showerror("error", 'Width should be greater than 8')
            elif self.__N <= 2:
                messagebox.showerror("error", 'Height should be greater than 8')
            elif self.__amountOfMines <= 0 or self.__amountOfMines > self.__M * self.__N:
                messagebox.showerror("error", 'Incorrect amount of mines')
            elif self.__N > 15:
                messagebox.showerror("error", 'Width should be lower than 15')
            elif self.__M > 15:
                messagebox.showerror("error", 'Height should be lower than 15')
            else:
                self.__boo1 = True

            if self.__boo1:
                self.newWindow = tkinter.Toplevel(self.master)
                self.app = game.Play(self.newWindow, self.__N, self.__M, self.__amountOfMines)

        except ValueError:
            messagebox.showerror("error", 'This is NOT an integer number!')




def main():
    root = tkinter.Tk(className='Saper')

    MainWindow(root)

    root.mainloop()


if __name__ == '__main__':

    main()