def maxi(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Значения равны"


try:
    while True:
        print(maxi(float(input("Число 1:")), float(input("Число 2:"))))
except:
    input("Дебил! Вводи данные нормально!\nДля выхода нажми enter...")
