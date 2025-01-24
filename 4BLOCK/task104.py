day_num = int(input("Введите номер дня недели (1-7): "))

def day(day_num):
    match day_num:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            return "Такого дня недели не существует"

print(day(day_num))
