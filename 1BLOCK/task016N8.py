from math import sin, radians
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
otvet = a / round(sin(radians(b)), 2)
print(f"Ваш ответ: {otvet}")