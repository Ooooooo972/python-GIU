from tkinter import *
root = Tk()
lbl = Label(root, text = "Hello")
lbl.grid()

def clicked():
    lbl.configure(text = "Clicked")

btn = Button(root, text = "Click", command = clicked)
btn.grid()
root.mainloop()