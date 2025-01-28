def calculate_age(birth_year, birth_month, current_year, current_month):
    full_years = current_year - birth_year
    full_months = current_month - birth_month

    if full_months < 0:
        full_years -= 1
        full_months += 12

    return full_years, full_months


birth_year = int(input("Введите год рождения: "))
birth_month = int(input("Введите месяц рождения: "))
current_year = int(input("Введите конкретный год: "))
current_month = int(input("Введите конкретный месяц: "))

age_years, age_months = calculate_age(birth_year, birth_month,
                                      current_year, current_month)
print(f"Полный возраст: {age_years}. Полных месяцев: {age_months}")
