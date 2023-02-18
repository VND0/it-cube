from tkinter import *

# Создание окна и задание его параметров
root = Tk()
root.title("Добавление текста")
root.resizable(False, False)


def add_text():
    """Добавление текста"""
    txt = enter.get()
    if txt:
        text_field.insert(END, txt + "\n")


def clear_text():
    """Очистка текстового поля"""
    text_field.delete(0.0, END)    # Оказвается, сюда нужно давать float индексы. Также подойдет 1.0 как index1


# Создание элементов
welcome = Label(root, text="Введите текст", font=("Helvetica", 15))
enter = Entry(root, width=20, font=("Helvetica", 15))
add = Button(root, text="Добавить", command=add_text, font=("Helvetica", 15))
clear = Button(root, text="Очистить", command=clear_text, font=("Helvetica", 15))
text_field = Text(root, height=22, width=50, font=("Helvetica", 15))

# Расположение элементов в окне
welcome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
enter.grid(row=1, column=0, padx=5, pady=5, sticky="w")
add.grid(row=2, column=0, padx=5, pady=5, sticky="w")
text_field.grid(row=3, column=0, padx=5, pady=5)
clear.grid(row=4, column=0, padx=5, pady=5, sticky="w")

# Запуск окна
root.mainloop()
