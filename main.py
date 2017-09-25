from tkinter import *

root = Tk()

def printName():
    print("Hello my name is Shane!")

def printName2(event):
    print("Hello again!")

button_1 = Button(root, text="Print Name", command=printName)
button_1.pack()

button_2 = Button(root, text="Printt Name 2")
button_2.bind("<Button-1>", printName2)
button_2.pack()

root.mainloop()
