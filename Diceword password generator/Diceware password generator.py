from random import SystemRandom
import re
from tkinter import *
from tkinter.messagebox import *


#gets a random number from 1 to 6 as dice throw
def get_number():
    rand = SystemRandom()
    num = rand.randint(1,6)
    return str(num)

#gets index consisting of 5 dice throws
def get_index():
    index = ''
    for i in range(5):
        dice = get_number()
        index += dice
    return index

#gets a word from a correct index in a dictionary
def get_word(index):
    with open('list.txt', 'r') as file:
        data = file.read()
        inds = re.findall(r'\d{5}',data)
        words = re.findall(r'[a-z]+',data)
    diceWare = {}
    x = 0
    for i in inds:
        diceWare[i] = words[x]
        x+=1
    return diceWare[index]

#gets passpharse of wanted numbers of words
def get_passphrase(number):
    passph = ''
    for i in range(number):
        word = get_word(get_index()) + ' '
        passph += word

    return passph



# copy text to clipboard
def copy():
    field_value = blank.get()  # get field value from blank
    main.clipboard_clear()  # clear clipboard contents
    main.clipboard_append(field_value)  # append new value to clipbaord

#center the window
def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

##def load_text():
##    with open('welcome_text.txt', 'r') as file:
##        heading = file.read()
##        par1=file.readline()
##        par2=file.readline()
##        par3=file.readline()
##        end=file.readline()
##        data = [heading,par1,par2,par3,end]
##    return data
##
##def open_window(main):
##    text = load_text()
##    wrap = 300
##    Label(main, text = text[0], wraplength=wrap).grid(row=0)
##    Label(main, text = text[1], wraplength=wrap).grid(row=1)
##    Label(main, text = text[2], wraplength=wrap).grid(row=2)
##    Label(main, text = text[3], wraplength=wrap).grid(row=3)
##    Label(main, text = text[4], wraplength=wrap).grid(row=4)
##    button = Button(main, text='Ok', command=main.destroy, justify="center").grid(row=5, sticky=W, pady=4)
##    center(main)
##    return button

def main_window(main):
    def generate_ans():
        blank.delete(0, 'end') # clears the display window
        number = int(num1.get())
        passph = get_passphrase(number) # generates passphrase
        blank.insert(0, passph) # prints the outcome
    Label(main, text = "Enter number of words:").grid(row=0)
    Label(main, text = "The Passpharse is:").grid(row=1)
    num1 = Entry(main)
    blank = Entry(main, width='50')
    num1.grid(row=0, column=1)
    blank.grid(row=1, column=1)
    Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
    Button(main, text='Generate', command=generate_ans).grid(row=4, column=1, sticky=W, pady=4)
    Button(main, text='Copy', command=copy).grid(row=4, column=2, sticky=W, pady=4)
    center(main)    

main = Tk()
app = main_window(main)



mainloop()
