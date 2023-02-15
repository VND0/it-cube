from tkinter import *
from tkinter.ttk import Combobox

def place_val():
    res_output.delete()
    res_output.insert(n)


root = Tk()
root.geometry("500x500")
root.title("Program")

digits = Combobox(root)
digits.configure(values=(1, 2, 3, 4, 5))

letters = Combobox(root)
letters.configure(values=("a", "b", "c", "d", "e"))

res_output = Entry(root, width=3)

btn = Button(root, text="")

