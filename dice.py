# Dice Rolling using Python
# https://teamerror.net


import random
from tkinter import *

root = Tk()
root.geometry("250x250")
root.title("Dice Roll")

l1 = Label(root, text='', font=("times", 200))

def roll():
    numbers = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(numbers)}{random.choice(numbers)}', bg="white")
    l1.pack()

b1 = Button(root, text="Click To Roll", command=roll, bg="white")
b1.place(x=10, y=10)
b2 = Button(root, text="EXIT", command=quit, bg="white")
b2.place(x=150, y=10)

root.mainloop()















