from tkinter import *
root = Tk()
txt = Entry(root)
txt.grid()
txt.insert(0, "Geeks")
print(txt.get())