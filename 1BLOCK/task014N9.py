# синус а * косинус б + косинус а * синус б
from math import sin, cos, radians
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
otvet = round(sin(radians(a)), 2) * round(cos(radians(b)), 2) + round(cos(radians(a)), 2) * round(sin(radians(b)), 2)
print(f"Ваш ответ: {otvet}")