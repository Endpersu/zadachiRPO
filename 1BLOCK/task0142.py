# sin a
from math import sin, radians
a = int(input("Введите длину гипотенузу: "))
b = int(input("Введите длину противолежащего катета: "))
otvet = round(b/a)
print(f"Синус равен: {otvet}")

x = int(input("Введите число: "))
result = round(sin(radians(x)), 2)
print(f"Ваш ответ: {result}")