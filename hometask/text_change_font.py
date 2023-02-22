from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("Добавление текста")
root.resizable(False, False)
root.option_add('*TCombobox*Listbox.font', "Helvetica")
root.geometry("599x798")


def add_text():
    """Добавление текста"""
    text_field.configure(state=NORMAL)
    txt = enter.get()
    if txt:
        text_field.insert(END, txt + "\n")
    text_field.configure(state=DISABLED)


def clear_text():
    """Очистка текстового поля"""
    text_field.configure(state=NORMAL)
    text_field.delete(0.0, END)    # Оказывается, сюда нужно подавать float индексы. Также подойдет 1.0 как index1
    text_field.configure(state=DISABLED)


def change_font():
    """Изменение шрифта в Text"""
    text_field.configure(state=NORMAL)
    text_field.configure(font=(choose_font.get(), 15))
    text_field.configure(state=DISABLED)


# Создание элементов
welcome = Label(root, text="Введите текст", font=("Helvetica", 15))
enter = Entry(root, width=20, font=("Helvetica", 15))
add = Button(root, text="Добавить", command=add_text, font=("Helvetica", 15))
clear = Button(root, text="Очистить", command=clear_text, font=("Helvetica", 15))

text_field = Text(root, height=21, width=30, font=("Helvetica", 15))
text_field.configure(state=DISABLED)

choose_font = Combobox(root, font=("Helvetica", 15), state="readonly")
choose_font.configure(values=("Helvetica", "Arial", "Segoe UI", "Calibri"))
choose_font.current(0)

font_btn = Button(root, text="Change color", command=change_font, font=("Helvetica", 15))

# Расположение элементов в окне
welcome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
enter.grid(row=1, column=0, padx=5, pady=5, sticky="w")
add.grid(row=2, column=0, padx=5, pady=5, sticky="w")
text_field.grid(row=3, column=0, padx=5, pady=5)
clear.grid(row=4, column=0, padx=5, pady=5, sticky="w")
font_btn.grid(row=2, column=1, padx=5, pady=5)
choose_font.grid(row=3, column=1, padx=5, pady=5, sticky="n")

# Запуск окна
root.mainloop()
