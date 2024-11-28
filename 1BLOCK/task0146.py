## 5 * косинус y
from math import cos, radians
y = int(input("Введите число: "))
otvet = 5 * round(cos(radians(y)), 2)
print(f"Ваш ответ: {otvet}")