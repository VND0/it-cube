from tkinter import *


def uc(txt):



def change_case(txt):
    arr = []
    for i in txt:
        if i.isalpha():
            if i == i.lower():
                arr.append(i.upper())
            else:
                arr.append(i.lower())
        else:
            arr.append(i)
    arr = "".join(arr)
    name.delete(0, END)
    name.insert(END, arr)
    return arr


def read():
    f = open(name.get(), "r")
    txt.insert("1.0", f.read())


def write():
    text = txt.get("1.0", END)
    f = open(name.get(), "w")
    for i in text:
        f.write(i)
    f.close()


root = Tk()
root.geometry("650x400")
root.title("Program")
stfon = ("Cousine", 16)

txt = Text(root, width=30, height=10, font=stfon)
btn1 = Button(root, text="Считать", font=stfon, bg="#8acbde", command=read)
btn2 = Button(root, text="Записать", font=stfon, bg="#31ebd3", command=write)
l1 = Label(root, text="Имя:", font=stfon)
name = Entry(root, width=10, font=stfon, bg="#00FF00")

txt.grid(row=0, column=0, padx=5, pady=5, rowspan=10)
btn1.grid(row=0, column=1, padx=5, pady=5, sticky=N)
btn2.grid(row=0, column=2, padx=5, pady=5, sticky=N)
l1.grid(row=1, column=1, padx=5, pady=5, sticky=N)
name.grid(row=1, column=2, padx=5, pady=5, sticky=N)

root.mainloop()
