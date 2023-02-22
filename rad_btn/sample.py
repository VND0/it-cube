from tkinter import *
from tkinter.ttk import Radiobutton

root = Tk()
root.title("Trying radiobutton")
root.geometry("300x300")

python = "Python"
java = "Java"
javascript = "JavaScript"

lang = StringVar(value=python)

header = Label(root, textvariable=lang)
header.grid(row=0, column=1, padx=5, pady=5, sticky=W)

py_btn = Radiobutton(root, text=python, value=python, variable=lang)
py_btn.grid(row=2, column=1, padx=5, pady=5, sticky=W)

jv_btn = Radiobutton(root, text=java, value=java, variable=lang)
jv_btn.grid(row=3, column=1, padx=5, pady=5, sticky=W)

js_btn = Radiobutton(root, text=javascript, value=javascript, variable=lang)
js_btn.grid(row=4, column=1, padx=5, pady=5, sticky=W)

root.mainloop()
