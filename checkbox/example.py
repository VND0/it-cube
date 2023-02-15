from tkinter import *
from tkinter.ttk import Checkbutton


def qqq():
    if enabled.get() == 0:
        en2.delete(0, END)
        en2.insert(0, int(en.get()))
    elif enabled.get() == 1:
        en2.delete(0, END)
        en2.insert(0, int(en.get()) * 2)


root = Tk()
root.title("Моя программа")
root.geometry("650x400")
glc = "#FFB540"
root.configure(bg=glc)
sf = ("Calibri", 25)

en = Entry(root, width=10, font=sf)
en.grid(column=0, row=0, padx=5, pady=5)

bt = Button(root, text="Умножить", font=("Calibri", 20), command=qqq)
bt.grid(column=1, row=0, padx=5, pady=5)

en2 = Entry(root, width=10, font=sf)
en2.grid(column=1, row=1, padx=5, pady=5)

enabled = IntVar()
enabled.set(0)
chb = Checkbutton(root, text="умножить на два", variable=enabled)
chb.grid(column=0, row=1, padx=5, pady=5)

root.mainloop()
