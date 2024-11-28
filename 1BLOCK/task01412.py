## -5 * x в корне + y в корне
import math
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
otvet = -5 * round(math.sqrt(x + round(math.sqrt(y))))
print(f"Ваш ответ: {otvet}")