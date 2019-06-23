#!/usr/bin/python

# A slightly fancier useless widget.

# Simple button demo.
from Tkinter import *

# Brighten a color by hex 101010 and return the modified color.
def brighten(c):
    ret = '#'
    for s in [ 1, 3, 5]:
        ret = ret + '%02x' % (min(int(c[s:s+2],16) + 0x10, 0xff),)
    return ret

# List of button colors
bcolors = [ '#AA4422', '#33DD11', '#4433EE', '#AA22EE' ]

# Change the label text.  Changes the color of the button in rotation.
def changebut():
    global bcolors
    color = bcolors.pop();
    bcolors = [ color ] + bcolors
    but.configure(background=color, activebackground=brighten(color))

# Create the GUI.
root = Tk()
lab = Label(root, text="Press Below", background='#FF3311', relief='ridge')
lab.grid(row=0, column=0)
but = Button(root, text="Push Me", command=changebut)
changebut()
but.grid(row=1, column=0)
root.mainloop()
