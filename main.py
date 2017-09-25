from tkinter import *

def doNothing():
    print("Do nothing.")

root = Tk()

m = Menu(root)
root.config(menu=m)

subm = Menu(m)
m.add_cascade(label="File", menu=subm)
subm.add_command(label="New Project", command=doNothing)
subm.add_separator()
subm.add_command(label="New", command=doNothing)

subm2 = Menu(m)
m.add_cascade(label="Edit", menu=subm2)
subm2.add_command(label="Redo", command=doNothing)

root.mainloop()
