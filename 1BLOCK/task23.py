from math import sqrt

a = int(input("Введите число a: "))
otvet = (a * a + 10) / (sqrt(a * a + 1))
print(f"Ваш ответ: {otvet}")