
#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

import tkinter as tk
def yash():
	print("HELLO WORLD!")
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame, text="QUIT", fg="red",command=quit)
button.pack(side=tk.LEFT)
Nainiwal = tk.Button(frame,text="Hello",command=yash)
Nainiwal.pack(side=tk.LEFT)
Nainiwal.mainloop()



#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.

import tkinter
from tkinter import*
root=Tk()
b=Button(root,text='quit',fg='red',command=quit)
b.pack()
b1=Button(root,text='hello world',width=20)
b1.pack()
root.mainloop()

#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

import tkinter
from tkinter import *
import sys

def exit():
    sys.exit()


def click():
    a.config(text="WELCOME!")


root=Tk()
root.geometry("400x400")

a=Label(root,text="HELLO WORLD !",width=150,fg="red")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

b1=Button(f1,width=30,text="exit!",bg="blue",command=exit)
b1.pack()

b2=Button(f1,width=30,text="label",bg="black",command=click)
b2.pack()

root.mainloop()







#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.

import tkinter
from tkinter import*
def show():
	print(entry.get())
root=Tk()
entry=Entry(root,width=20)
entry.pack()
b=Button(root,text='click',width=20,command=show)
b.pack()
root.mainloop()