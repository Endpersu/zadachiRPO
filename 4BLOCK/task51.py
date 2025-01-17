def can_fit(a, b, c, d):
    return (c + 2 <= a and d + 2 <= b) or (d + 2 <= a and c + 2 <= b)


a = float(input("Введите ширину конверта (мм): "))
b = float(input("Введите высоту конверта (мм): "))
c = float(input("Введите ширину открытки (мм): "))
d = float(input("Введите высоту открытки (мм): "))

if can_fit(a, b, c, d):
    print("Открытка войдет в конверт.")
else:
    print("Открытка не войдет в конверт.")
