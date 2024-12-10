from math import pi
r = int(input("Введите радиус: "))
c = round(2 * pi * r, 2)
s = round(pi * (r ** 2), 2)
print(f"Длина окружности = {c}")
print(f"Площадь круга = {s}")
