from tkinter import *

class App:
    def __init__(self, master):
        self.counter = 0
        self.master = master
        
        self.master.minsize(width=200, height=200)
        self.master.maxsize(width=200, height=200)

    def createText(self):
        self.counter_text = Label(self.master, text="0")
        self.counter_text.grid(row=0, column=1)

    def createButtons(self):
        self.inc_button = Button(self.master, text="Increase", command=self.incCounter)
        self.dec_button = Button(self.master, text="Decrease", command=self.decCounter)

        self.inc_button.grid(row=0, column=0)
        self.dec_button.grid(row=0, column=2)

    def incCounter(self):
        self.counter += 1
        self.counter_text.config(text=str(self.counter))

    def decCounter(self):
        self.counter -= 1
        self.counter_text.config(text=str(self.counter))

root = Tk()

app = App(root)
app.createText()
app.createButtons()

root.mainloop()
