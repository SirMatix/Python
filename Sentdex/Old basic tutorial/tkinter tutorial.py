from tkinter import *

from Pillow import Image, ImageTk

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title('GUI')
        self.pack(fill=BOTH, expand=1)
        #quit button text
        #quitButton = Button(self, text='QUIT', command=self.client_exit)
        #top left button placement
        #quitButton.place(x=0, y=0)
        #menu of the main window, menu is made by us, Menu is part of tkinter module
        menu = Menu(self.master)
        self.master.config(menu=menu)
        #dodawanie wysuwanego menu
        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Image', command=self.showTxt)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)
    def showTxt(self):
        text = Label(self, text='Hey This is text')
        text.pack()
    def client_exit(self):
        exit()
    def showImg(self):
        load = Image.open('Aaron.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

root = Tk()
#window size
root.geometry('400x300')

app = Window(root)

root.mainloop()
