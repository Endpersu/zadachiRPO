## 3 синус * 2 а * косинус 3 * b
from math import cos, sin, radians
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
otvet = 3 * round(sin(radians(2 * a)), 2) * round(cos(radians(3 * b)), 2)
print(f"Ваш ответ: {otvet}")