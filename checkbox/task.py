from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

fruit_call = {"Яблоки": 0.52, "Бананы": 0.89, "Персики": 0.39, "Киви": 0.61}
error_text = """Не выбран фрукт или в поле ввода массы указано неверное значение: 
либо нечисловые значения, 
либо поле оставлено пустым, 
либо в качестве разделителя десятичной дроби использована запятая (должна быть точка),
либо масса отрицательная."""


def get_value():
    # Если галочки нет
    if not (bool(status.get())):
        result.configure(state=NORMAL)
        result.delete(0, END)
        try:
            per_1_g = fruit_call[fruits.get()]

            mass_to_work_raw = mass.get()
            mass_to_work = ""
            if not(mass_to_work_raw.isdigit()):
                final = ""
                for i in mass_to_work_raw:
                    if i.isdigit():
                        final += i
                    else:
                        break
                mass_to_work = float(final)
            else:
                mass_to_work = float(mass_to_work_raw)

            if mass_to_work < 0:
                0/0
            result.insert(0, round(per_1_g * mass_to_work, 2))
        except:
            messagebox.showerror("Ошибка ввода данных", error_text)
        result.configure(state=DISABLED)
    # Если галочка стоит
    else:
        result.configure(state=NORMAL)
        result.delete(0, END)
        work_with_percents = 0
        try:
            per_1_g = fruit_call[fruits.get()]

            mass_to_work_raw = mass.get()
            mass_to_work = ""
            if not(mass_to_work_raw.isdigit()):
                final = ""
                for i in mass_to_work_raw:
                    if i.isdigit():
                        final += i
                    else:
                        break
                mass_to_work = float(final)
            else:
                mass_to_work = float(mass_to_work_raw)

            if mass_to_work < 0:
                0/0

            work_with_percents = round(per_1_g * mass_to_work, 2)
            normal_for_adult = 2500
            result.insert(0, round(work_with_percents / normal_for_adult * 100, 2))
        except:
            messagebox.showerror("Ошибка ввода данных", error_text)
        result.configure(state=DISABLED)


root = Tk()
root.title("Расчет каллорий фруктов")
root.geometry("750x200")
root.option_add('*TCombobox*Listbox.font', "Calibri")    # *TCombobox*Listbox.font - опция окна для шрифта Combobox
root.resizable(False, False)

fruits = Combobox(root, values=("Фрукты", "Яблоки", "Бананы", "Персики", "Киви"), font=("Calibri", 20))
fruits.configure(state="readonly")
fruits.current(0)

mass = Entry(root, width=15, font=("Calibri", 20))

unit = Label(root, text="граммов", font=("Calibri", 20))

unit_result = Label(root, text="ккал или %", font=("Calibri", 20))

btn = Button(root, text="Вычислить", command=get_value, font=("Calibri", 20))

result = Entry(root, width=15, font=("Calibri", 20))

# процент от суточной нормы
status = IntVar()
status.set(0)
box = Checkbutton(root, text="Вычислить процент от суточной нормы", variable=status, font=("Calibri", 15))

# расположение в окне
fruits.grid(row=0, column=0, padx=5, pady=5, sticky="w")
mass.grid(row=0, column=1, pady=5)
unit.grid(row=0, column=2, pady=5, sticky="w")
btn.grid(row=1, column=0, padx=5, pady=5, sticky="w")
result.grid(row=1, column=1, pady=5)
unit_result.grid(row=1, column=2, pady=5)
box.grid(column=0, row=3, padx=5, pady=5)

root.mainloop()
