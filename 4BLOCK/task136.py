def day_of_year(k, start_day):
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    day_index = (start_day - 1 + (k - 1)) % 7
    day = days[day_index]

    if day in ['суббота', 'воскресенье']:
        return f"{k}-й день года: {day}"
    else:
        return f"{k}-й день года: рабочий день ({day})"


k = int(input("Введите номер дня года (1-365): "))
start_day = 1
result = day_of_year(k, start_day)
print(result)


def day_of_year_d(k, d):
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    day_index = (d - 1 + (k - 1)) % 7
    day = days[day_index]

    if day in ['суббота', 'воскресенье']:
        return f"{k}-й день года: {day}"
    else:
        return f"{k}-й день года: рабочий день ({day})"


k = int(input("Введите номер дня года (1-365): "))
d = int(input("Введите номер дня недели (1 - понедельник, ..., 7 - воскресенье): "))
result_d = day_of_year_d(k, d)
print(result_d)
