def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    print("Выберите конвертацию:")
    print("1: Цельсий в Фаренгейт")
    print("2: Фаренгейт в Цельсий")

    choice = input("Введите номер операции (1 или 2): ")

    if choice == '1':
        celsius = float(input("Введите температуру в градусах Цельсия: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C равно {fahrenheit}°F")

    elif choice == '2':
        fahrenheit = float(input(
            "Введите температуру в градусах Фаренгейта: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F равно {celsius}°C")

    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")


if __name__ == "__main__":
    main()
