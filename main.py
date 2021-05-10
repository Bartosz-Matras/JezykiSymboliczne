#====================================
#             Saper
#      Autor: Bartosz Matras
#====================================


#=================Lib================
import tkinter
from PIL import Image, ImageTk

class mainWindow:
    def __init__(self, master):
        self.N = None
        self.M = None
        self.master = master
        self.master.configure(bg='grey')
        self.master.geometry('350x200')
        self.master.resizable(0, 0)
        self.master.iconphoto(False, tkinter.PhotoImage(file=r'icon.png'))

        self.frame = tkinter.Frame(self.master)

        self.buttonPlay = tkinter.Button(self.frame, text='Play', width=25, height=4, bg='snow', command=lambda:self.clicked())
        self.buttonQuit = tkinter.Button(self.frame, text='Quit', width=25, height=4, bg='snow', command=lambda:self.close_window())
        self.labelAuthor = tkinter.Label(self.frame, text='Author: Bartosz Matras', width=26, bg='grey')

        self.frame.pack()
        self.buttonPlay.pack()
        self.buttonQuit.pack()
        self.labelAuthor.pack()

    def clicked(self):
        self.buttonPlay.destroy()
        self.buttonQuit.destroy()
        self.labelAuthor.destroy()

        self.label1 = tkinter.Label(self.master, text='Enter n: ', bg='grey')
        self.text1 = tkinter.Text(self.master, height=1, width=5, padx=10, pady=5)

        self.label2 = tkinter.Label(self.master, text='Enter m: ', bg='grey')
        self.text2 = tkinter.Text(self.master, height=1, width=5, padx=10, pady=5)

        self.buttonQuit2 = tkinter.Button(self.frame, text='Quit', width=10, height=2, bg='snow', command=lambda: self.close_window())
        self.submit = tkinter.Button(self.frame, text='Submit', width=10, heigh=2, bg='snow', command=lambda:self.clicked2())

        self.label1.pack()
        self.text1.pack()
        self.label2.pack()
        self.text2.pack()
        self.submit.pack()
        self.buttonQuit2.pack(side=tkinter.BOTTOM)

    def close_window(self):
        self.master.destroy()

    def clicked2(self):
        # self.label3.destroy()
        try:
            self.N = int(self.text1.get("1.0", "end-1c"))
            self.M = int(self.text2.get("1.0", "end-1c"))
            self.submit.destroy()
            self.newWindow = tkinter.Toplevel(self.master)
            self.app = Play(self.newWindow, self.N, self.M)
            # self.master.destroy()
        except:
            self.label3 = tkinter.Label(self.master, text="This is NOT an integer number!", bg='grey')
            self.label3.pack()

class Play:
    def __init__(self, master, N, M):
        self.N = N
        self.M = M
        self.master = master
        self.master.geometry('680x500')
        self.master.resizable(0, 0)
        self.master.iconphoto(False, tkinter.PhotoImage(file=r'icon.png'))

        self.frame = tkinter.Frame(self.master)

        self.mines = tkinter.Label(self.master, bg='grey', fg='red2', font=('BOLD', 30))
        self.mines.grid(row=0, column=0)
        self.mines['text'] = '0100'

        self.timer = tkinter.Label(self.master, bg='grey', fg='red2', font=('BOLD', 30))
        self.timer.grid(row=0, column=self.M - 1)
        self.timer['text'] = '0001'

        # self.mines.pack()
        # self.frame.pack()

    def buttons(self):




def main():
    root = tkinter.Tk(className='Saper')

    app = mainWindow(root)


    root.mainloop()


if __name__ == '__main__':

    main()