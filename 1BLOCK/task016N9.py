from math import sin, radians
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
x = int(input("Введите третье число: "))
otvet = 1/2 * a * b * round(sin(radians(x)), 2)
print(f"Ваш ответ: {otvet}")