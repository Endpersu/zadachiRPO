from math import cos, radians
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = (2 * b * c * round(cos(radians(b)), 2)) / (b+c)
print(f"Ваш ответ: {otvet}")