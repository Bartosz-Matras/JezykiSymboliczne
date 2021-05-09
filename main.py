#====================================
#             Saper
#      Autor: Bartosz Matras
#====================================


#=================Lib================
import tkinter

##==============Window===============
def myWindow():
    window = tkinter.Tk()
    window.title("Saper")
    window.iconphoto(False, tkinter.PhotoImage(file=r'Img\icon.png'))
    window.geometry('680x500')
    window.resizable(0, 0)
    return window

def gameWindow():
    window = tkinter.Tk()
    window.title("Saper")
    window.iconphoto(False, tkinter.PhotoImage(file=r'Img\icon.png'))
    window.geometry('680x500')
    window.resizable(0, 0)
    return window


##=========Button function===========
def clearFrame():
    for widgets in window.winfo_children():
        widgets.destroy()

def destroy():
    window.destroy()
    global logic1
    logic1 = True
    gameWindow()

##===============Menu================
def myMenu(window):
    menu = []

    def retrive_input():
        try:
            global N
            global M
            N = int(en1.get("1.0", "end-1c"))
            M = int(en2.get("1.0", "end-1c"))
        except ValueError:
            print("This is NOT an integer number!")


    label2 = tkinter.Label(window, text="Enter n and m: ").pack()
    menu.append(label2)

    en1 = tkinter.Text(window, height=2, width=5)
    en1.pack()
    en2 = tkinter.Text(window, height=2, width=5)
    en2.pack()

    buttonSubmit = tkinter.Button(window, text='Subbmit', padx=48, pady=10, command=lambda: retrive_input()).pack()
    menu.append(buttonSubmit)

    buttonNewWindow = tkinter.Button(window, text='Play', padx=60, pady=10, command=destroy).pack()
    menu.append(buttonNewWindow)

    buttonExit = tkinter.Button(window, text='Exit', padx=60, pady=10, bg='red', command=exit)
    buttonExit.pack(side=tkinter.BOTTOM)

    return menu

##=============TopBar================
def topBar(window):
    top = []

    bombCounter = tkinter.Label(window)
    bombCounter.grid(row=0, column=0)
    bombCounter['text'] = '0100'
    top.append(bombCounter)

    timer = tkinter.Label(window)
    timer.grid(row=0, column=M)
    top.append(timer)

    return top


##===============Main================
if  __name__ == '__main__':
    N = None
    M = None
    logic1 = False

    window = myWindow()

    ## Display menu
    menu = myMenu(window)

    if logic1:
        window.destroy()
        window = gameWindow()
        game = topBar(window)

    window.mainloop()
