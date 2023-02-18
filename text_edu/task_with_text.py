from tkinter import *

# Создание окна и задание его параметров
root = Tk()
root.title("Добавление текста")
root.resizable(False, False)
# Geometry нет, т.к. Текстовое поле и так нормально задает размер окна


def add_text():
    """Добавление текста"""
    txt = enter.get()
    if txt:
        text_field.insert(END, txt + "\n")


def clear_text():
    """Очистка текстового поля"""
    text_field.delete(0.0, END)    # Оказвается, сюда нужно подавать float индексы. Также подойдет 1.0 как index1


# Создание элементов
welcome = Label(root, text="Введите текст", font=("Helvetica", 15))                 # Label, "призывающий" вводить текст
enter = Entry(root, width=20, font=("Helvetica", 15))                               # Поле ввода текста
add = Button(root, text="Добавить", command=add_text, font=("Helvetica", 15))       # Кнопка добавления текста
clear = Button(root, text="Очистить", command=clear_text, font=("Helvetica", 15))   # Кнопка очистки текстового поля
text_field = Text(root, height=22, width=50, font=("Helvetica", 15))                # Поле вывода текста на экран

# Расположение элементов в окне
welcome.grid(row=0, column=0, padx=5, pady=5, sticky="w")    # Label, строка 0, колонка 0, прижата к левому краю клетки
enter.grid(row=1, column=0, padx=5, pady=5, sticky="w")      # Entry, строка 1, колонка 0, прижата к левому краю клетки
add.grid(row=2, column=0, padx=5, pady=5, sticky="w")        # Button, строка 2, колонка 0, прижата к левому краю клетки
text_field.grid(row=3, column=0, padx=5, pady=5)             # Text, строка 3, колонка 0, в центре занимаемых клеток
clear.grid(row=4, column=0, padx=5, pady=5, sticky="w")      # Button, строка 4, колонка 0, прижата к левому краю клетки

# Запуск окна
root.mainloop()
