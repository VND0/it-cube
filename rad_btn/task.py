from tkinter import *
from tkinter.ttk import Radiobutton


def print_to_text():
    if int(variant.get()):
        width = int(variant.get())
        height = int(variant.get())
    else:
        width = int(en_w.get())
        height = int(en_h.get())

    field.configure(state=NORMAL)
    field.delete(0.0, END)
    for i in range(height):
        if i == 0 or i == height-1:
            field.insert(float(i), "#" * width + "\n")
        else:
            field.insert(float(i), ("#" + " " * (width-2) + "#" + "\n"))
    field.configure(state=DISABLED)


root = Tk()
root.title("Generate a square")
glob_ft = ("Segoe UI", 15)

field = Text(root, width=30, height=30, font=glob_ft, state=DISABLED)

var4x4 = "4 x 4"
var5x5 = "5 x 5"
var6x6 = "6 x 6"
variant = StringVar()

btn4 = Radiobutton(root, text=var4x4, value=4, variable=variant, command=print_to_text)
btn5 = Radiobutton(root, text=var5x5, value=5, variable=variant, command=print_to_text)
btn6 = Radiobutton(root, text=var6x6, value=6, variable=variant, command=print_to_text)

lbl = Label(root, text="x")
en_w = Entry(root, width=2, font=glob_ft)
en_h = Entry(root, width=2, font=glob_ft)
custom = Radiobutton(root, value=0, variable=variant, command=print_to_text)

field.grid(row=0, column=0, padx=5, pady=5, rowspan=10, columnspan=10)
btn4.grid(row=0, column=11, padx=5, pady=5)
btn5.grid(row=1, column=11, padx=5, pady=5)
btn6.grid(row=2, column=11, padx=5, pady=5)

root.mainloop()
