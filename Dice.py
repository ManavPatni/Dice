###############################################################
#                                                             #
#               #  Created by ManavPatni                      #
#               #  Follow me on Github                        #
#               #  Visit my website                           #          
#               #  https://fireframe.godaddysites.com/        #
#                                                             #
###############################################################

# importing libraries into projects
import tkinter as tk
from tkinter import *
from tkinter import Button
from tkinter import font
import random

# this function will show random number between 1 to 6
def roll():
 a = random.randint(1,6)
 mynumber.set(a)

# this will desing the gui
root = tk.Tk()
root.geometry("200x100")
root.title("Dice")
root.minsize(200, 100)
root.maxsize(200, 100)

# this will show the result
mynumber = StringVar()
label = Label(text="", textvariable=mynumber, font="88888").pack(padx=15,pady=5)

# the button the will run the random number function
dice = Button(root, text="Roll Dice", command=roll).pack(side=BOTTOM, padx=15, pady=20)

root.mainloop()