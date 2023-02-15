from tkinter import *

root = Tk()
root.title("From lowercase to uppercase")
root.geometry("400x300")
ft = "Times Nem Roman"
root.configure(bg="#0000CC")


def convert():
    up_output.delete(0, END)
    up_output.insert(0, low_input.get().upper())


low_input = Entry(root, width=25, font=(ft, 20), bg="#C0C0C0")
low_input.grid(row=0, column=0, padx=10, pady=10)

conv = Button(root, text="Конвертировать", command=convert, font=(ft, 20), bg="#FF3333")
conv.grid(row=1, column=0, padx=10, pady=10)

res_txt = Label(root, text="В верхнем регистре", font=(ft, 20), bg="#FF3333")
res_txt.grid(row=3, column=0, padx=10, pady=10)

up_output = Entry(root, width=25, font=(ft, 20), bg="#C0C0C0")
up_output.grid(row=4, column=0, padx=10, pady=10)

root.mainloop()
