#====================================
#             Saper
#      Autor: Bartosz Matras
#====================================


#=================Lib================
import tkinter


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

        self.N = None
        self.M = None
        self.master = master
        self.master.configure(bg='grey')
        self.master.geometry('410x200')
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

        self.label1 = tkinter.Label(self.master, text='Enter n: ', bg='grey', height=1, width=10, pady=10)
        self.text1 = tkinter.Text(self.master, height=1, width=10, padx=20, pady=8)

        self.label2 = tkinter.Label(self.master, text='Enter m: ', bg='grey', height=1, width=10, pady=10)
        self.text2 = tkinter.Text(self.master, height=1, width=10, padx=20, pady=8)

        self.buttonQuit2 = tkinter.Button(self.master, text='Quit', width=10, height=2, bg='snow', command=lambda: self.close_windowYesNo2())
        self.submit = tkinter.Button(self.master, text='Submit', width=10, heigh=2, bg='snow', command=lambda: self.clicked2())

        self.label1.grid(row=0, column=0)
        self.text1.grid(row=0, column=1)
        self.label2.grid(row=0, column=2)
        self.text2.grid(row=0, column=3)
        self.submit.grid(row=1, columnspan=4, pady=10)
        self.buttonQuit2.grid(row=2, columnspan=4, pady=10)

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
            self.N = int(self.text1.get("1.0", "end-1c"))
            self.M = int(self.text2.get("1.0", "end-1c"))
            self.submit.destroy()
            self.newWindow = tkinter.Toplevel(self.master)
            self.app = Play(self.newWindow, self.N, self.M)

        except ValueError:
            self.label3 = tkinter.Label(self.master, text="This is NOT an integer number!", bg='grey')
            self.label3.grid(row=3, columnspan=4)


class Play:
    def __init__(self, master, N, M):
        self.N = N
        self.M = M
        self.time = 0
        self.master = master
        # self.master.geometry('%dx%d+100+100' % (self.N * 50, self.M * 25))
        # self.master.resizable(0, 0)
        self.master.iconphoto(False, tkinter.PhotoImage(file=r'icon.png'))

        self.frame = tkinter.Frame(self.master)

        self.mines = tkinter.Label(self.master, bg='grey', fg='red2', font=('BOLD', 30))
        self.mines.grid(row=0, column=0, padx=35, pady=10)
        self.mines['text'] = '0100'

        # self.start = tkinter.Button(self.master, text='Start', width=15, height=2, bg='snow', command=lambda: self.buttonsFun())
        # self.start.grid(row=0, column=self.M // 2)

        self.timer = tkinter.Label(self.master, bg='grey', fg='red2', font=('BOLD', 30))
        self.timer.grid(row=0, column=self.M-4)
        # self.timer['text'] = '0001'
        self.clock()

        self.emptyLabel = tkinter.Label(self.master, text=' ')
        self.emptyLabel.grid(row=1, columnspan=self.M)

        self.frame.grid(row=2, columnspan=M)

        buttons = [tkinter.Button(self.frame, height=1, width=2) for i in range(self.N * self.M)]

        for i in range(self.N):
            for j in range(self.M):
                if j == 0:
                    buttons[i * self.M + j].grid(row=i + 1, column=j, padx=(20, 0))
                elif j == self.M-1:
                    buttons[i * self.M + j].grid(row=i + 1, column=j, padx=(0, 20))
                else:
                    buttons[i * self.M + j].grid(row=i + 1, column=j)

    def clock(self):
        self.time += 1
        self.timer['text'] = '0'*(4 - len(str(self.time))) + str(self.time)
        self.master.after(1000, self.clock)


    # def buttonsFun(self):
    #     # self.start.destroy()
    #
    #     buttons = [tkinter.Button(self.frame, height=1, width=2) for i in range(self.N * self.M)]
    #
    #     for i in range(self.N):
    #         for j in range(self.M):
    #             buttons[i * self.M + j].grid(row=i+1, column=j)

def main():
    root = tkinter.Tk(className='Saper')

    app = mainWindow(root)

    root.mainloop()


if __name__ == '__main__':

    main()