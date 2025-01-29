def reverse_array(arr):
    return arr[::-1]


input_array = input("Введите числа через пробел: ")


numbers = list(map(int, input_array.split()))


reversed_numbers = reverse_array(numbers)


print(f"Массив в обратном порядке: {reversed_numbers}")
