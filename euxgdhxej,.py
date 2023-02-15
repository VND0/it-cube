from tkinter import *


# def clear_entry():
#     en.delete("0", END)


def save_n_print_n_clean():
    if en.get():
        print(en.get())
        en.delete("0", END)


root = Tk()
root.title("Edu")
root.geometry("800x800")

lbl = Label(root, text="Hello!", font=("Arial Bold", 25))
lbl.place(x=20, y=30)

en = Entry(root, width=30, font=("Arial Bold", 25))
en.place(x=40, y=80)
en.insert(0, "")

btn = Button(root, text="Print to console and clean", command=save_n_print_n_clean, font=("Arial Bold", 25))
btn.place(x=30, y=140)

root.mainloop()
