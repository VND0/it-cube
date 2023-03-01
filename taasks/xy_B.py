from tkinter import *
from tkinter import Radiobutton
from tkinter import messagebox

root = Tk()
root.title("Task")
global_ft = ("Cousine", 15)
root.resizable(False, False)


def compare():
    global val

    ans_ans.configure(state=NORMAL)
    ans_ans.delete(0, END)

    val = equation.get()
    try:
        x_got, y_got = float(x_ent.get()), float(y_ent.get())
        if val == "0":
            if 2 * x_got - 3 * y_got + 5 == 0:
                ans_ans.insert(END, "На прямой")
            else:
                ans_ans.insert(END, "Не на прямой")
        elif val == "1":
            if 4 * y_got - x_got == 0:
                ans_ans.insert(END, "На прямой")
            else:
                ans_ans.insert(END, "Не на прямой")
        if val == "2":
            if 5 * x_got - y_got - 3 == 0:
                ans_ans.insert(END, "На прямой")
            else:
                ans_ans.insert(END, "Не на прямой")
    except:
        messagebox.showerror(title="Ошибка ввода данных", message="Неверные значения переменных. \nВажно: в качестве разделителя дестяичной дроби используется не запятая, а точка. Возможно, проблема из-за этого.")
        equation.set(-1)

    ans_ans.configure(state=DISABLED)


equ1 = "2x-3y+5=0"
equ2 = "4y-x=0"
equ3 = "5x-y-3=0"

x_lbl = Label(root, text="x=", font=global_ft)
y_lbl = Label(root, text="y=", font=global_ft)
x_ent = Entry(root, width=5, font=global_ft)
y_ent = Entry(root, width=5, font=global_ft)

ans_lbl = Label(root, text="Ответ:", font=global_ft)
ans_ans = Entry(root, width=20, font=global_ft, state=DISABLED)

equation = StringVar(value=-1)

equ1_btn = Radiobutton(root, text=equ1, value=0, variable=equation, command=compare, font=global_ft)
equ2_btn = Radiobutton(root, text=equ2, value=1, variable=equation, command=compare, font=global_ft)
equ3_btn = Radiobutton(root, text=equ3, value=2, variable=equation, command=compare, font=global_ft)

equ1_btn.grid(row=0, column=0, padx=5, pady=5, sticky=W)
equ2_btn.grid(row=1, column=0, padx=5, pady=5, sticky=W)
equ3_btn.grid(row=3, column=0, padx=5, pady=5, sticky=W)

ans_lbl.grid(row=5, column=0, padx=0, pady=5, sticky=E)
ans_ans.grid(row=5, column=1, padx=0, pady=5, sticky=W)

x_lbl.grid(row=0, column=1, padx=0, pady=5, sticky=E)
y_lbl.grid(row=1, column=1, padx=0, pady=5, sticky=E)
x_ent.grid(row=0, column=2, padx=0, pady=5, sticky=W)
y_ent.grid(row=1, column=2, padx=0, pady=5, sticky=W)

root.mainloop()
