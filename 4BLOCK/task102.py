def determine_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4


x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))


if x != 0 and y != 0:
    quadrant = determine_quadrant(x, y)
    print(f"Точка ({x}, {y}) находится в {quadrant}-й четверти.")
else:
    print("Координаты не должны быть равны 0.")
