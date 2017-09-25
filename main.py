from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

line1 = canvas.create_line(0, 0, 200, 50)
line2 = canvas.create_line(0, 100, 100, 25, fill="red")

box1 = canvas.create_rectangle(20, 20, 50, 50, fill="green")

canvas.delete(line2)

root.mainloop()
