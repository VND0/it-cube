from tkinter import *
from tkinter.ttk import Combobox


def printing():
    lbl.configure(text=combo.get)


root = Tk()
root.title("Wi nd ow")
root.geometry("600x600")
# glob_cl = "FF99CC"
# root.configure(bg=glob_cl)

combo = Combobox(root, font=("Calibri", 20))
combo.configure(values=(1, 2, 3, 4, 5, "Текст"))
# combo.current()
combo.grid(column=0, row=1, padx=5, pady=5)
root.option_add('*TCombobox*Listbox.font', "Calibri")

lbl = Label(root, text="Выбери сочетание", font=("Calibri", 20))
lbl.grid(column=0, row=0, padx=5, pady=5)

combo2 = Combobox(root, font=("Calibri", 20))

root.mainloop()
