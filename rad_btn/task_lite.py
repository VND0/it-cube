from tkinter import *
from tkinter.ttk import Radiobutton
def print_to_text():
    field.delete(0.0, END)
    width, height = None, None
    if int(variant.get()):
        width = int(variant.get())
        height = int(variant.get())
    else:
        width = int(en_w.get())
        height = int(en_h.get())
    for i in range(height):
        if i == 0 or i == height-1:
            field.insert(END, "#" * width + "\n")
        else:
            field.insert(END, ("#" + " " * (width-2) + "#" + "\n"))
root = Tk()
root.title("Generate a square")
root.geometry("500x500")
glob_ft = ("Courier New", 15)
field = Text(root, width=30, height=15, font=glob_ft)
var4x4, var5x5, var6x6 = "4 x 4", "5 x 5", "6 x 6"
variant = StringVar()
btn4 = Radiobutton(root, text=var4x4, value=4, variable=variant, command=print_to_text)
btn5 = Radiobutton(root, text=var5x5, value=5, variable=variant, command=print_to_text)
btn6 = Radiobutton(root, text=var6x6, value=6, variable=variant, command=print_to_text)
lbl = Label(root, text="x")
en_w = Entry(root, width=2)
en_h = Entry(root, width=2)
custom = Radiobutton(root, value=0, variable=variant, command=print_to_text)
field.grid(row=0, column=0, padx=5, pady=5, rowspan=10, columnspan=10)
btn4.grid(row=0, column=11, padx=5, pady=5, sticky=W)
btn5.grid(row=1, column=11, padx=5, pady=5, sticky=W)
btn6.grid(row=2, column=11, padx=5, pady=5, sticky=W)
custom.grid(row=3, column=11, padx=5, pady=5, sticky=W)
en_w.grid(row=4, column=11, padx=0, pady=0, sticky=W)
lbl.grid(row=4, column=11, padx=0, pady=0)
en_h.grid(row=4, column=11, padx=0, pady=0, sticky=E)
root.mainloop()