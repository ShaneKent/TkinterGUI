from tkinter import *

def doNothing():
    print("Do nothing.")

root = Tk()

# Main Menu
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

# Toolbar

toolbar = Frame(root,  bg="blue")

insertButton = Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)

printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Status Bar

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
