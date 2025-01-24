month_num = int(input("Введите цифру месяца (от 1-12): "))


def month(month_num):
    match month_num:
        case 12:
            return "Декабрь"
        case 11:
            return "Ноябрь"
        case 10:
            return "Октябрь"
        case 9:
            return "Сентябрь"
        case 8:
            return "Август"
        case 7:
            return "Июль"
        case 6:
            return "Июнь"
        case 5:
            return "Май"
        case 4:
            return "Апрель"
        case 3:
            return "Март"
        case 2:
            return "Февраль"
        case 1:
            return "Январь"
        case _:
            return "Такого месяца нет"


print(month(month_num))
