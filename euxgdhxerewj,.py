from tkinter import *


def clear_entry():
    en.delete("0", END)


root = Tk()
root.title("Edu")
root.geometry("800x800")
root.configure(bg="#000000")

lbl = Label(root, text="Hello!", font=("Arial Bold", 25), fg="#23D416", bg="#3333FF")
lbl.place(x=20, y=30)

en = Entry(root, width=30, font=("Arial Bold", 25), fg="#3333FF", bg="#23D416")
en.place(x=40, y=80)
en.insert(0, "")

btn = Button(root, text="Clean", command=clear_entry, font=("Arial Bold", 25), fg="#CC00CC")
btn.place(x=30, y=140)

root.mainloop()
