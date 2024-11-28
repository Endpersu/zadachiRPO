## a * 2b в корне
import math
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
otvet = a * round(math.sqrt(2 * b))
print(f"Ваш ответ: {otvet}")