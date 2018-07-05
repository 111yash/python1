#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

import tkinter
from tkinter import *

root=Tk()
root.title("Dictionary")
root.geometry('200x200')
a=Label(root,text="Dictionary \nNames and Mobile Number",bg="blue")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

w=Scrollbar(f1,orient="vertical",)
w.pack(side=RIGHT,fill=Y)
mylist=Listbox(f1,width=30 , font=("Helvetica", 12),yscrollcommand=w.set)



d={"yash":111,"rajat":222,"vijay":567,"vivek":565,"rohan":657,"deepak":457,"deva":534,"suraj":456,"pandey":458,"dev":809}

for key in d:
    mylist.insert(END,'{}: {}'.format(key, d[key]))
mylist.pack(side=LEFT,fill=BOTH)
w.config(command=mylist.yview)
root.mainloop()






#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.
import tkinter
from tkinter import *

def show():
    k=entry.get()
    v=entry2.get()
    mylist.insert(END,'{}: {}'.format(k, v))
    d[k]=v
    print(d)

root=Tk()
root.title("Dictionary")
root.geometry('200x200')
a=Label(root,text="Dictionary \nNames and Mobile Number",bg="blue")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

w=Scrollbar(f1,orient="vertical",)
w.pack(side=RIGHT,fill=Y)
mylist=Listbox(f1,width=30 , font=("MT Bold", 12),yscrollcommand=w.set)



d={"gagan":987,"arayan":895,"nikunj":567,"harpreet":558,"bhuvi":576,"guru":447,"rohit":5345,"kamal":4568,"ram":4586,"sahil":809687}

for key in d:
    mylist.insert(END,'{}: {}'.format(key, d[key]))
mylist.pack(side=LEFT,fill=BOTH)
w.config(command=mylist.yview)

entry=Entry(root,width=20)
entry.pack()
entry2=Entry(root,width=20)
entry2.pack()
b=Button(root,text="insert",bg="pink",command=show)
b.pack()
root.mainloop()