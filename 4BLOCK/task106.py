month_num = int(input("Введите число месяца (от 1-12): "))

def season(month_num):
    match month_num:
        case 1 | 2 | 12:
            return "Зима"
        case 3 | 4 | 5:
            return "Весна"
        case 6 | 7 | 8:
            return "Лето"
        case 9 | 10 | 11:
            return "Осень"
        case _:
            return "Такого месяцы не существует, как и сезона"
        
print(season(month_num))