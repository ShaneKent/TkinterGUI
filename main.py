from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Shane is so cool.")

answer = tkinter.messagebox.askquestion("Question 1", "Say hello?")

if answer == "yes":
    print("Yes")
else:
    print("No")

root.mainloop()
