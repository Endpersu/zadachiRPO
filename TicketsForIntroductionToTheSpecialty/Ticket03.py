N = int(input("Введите целое положительное число N: "))
total_sum = 0


for i in range(1, N + 1):
    total_sum += i


print(f"Сумма всех целых чисел от 1 до {N} равна {total_sum}.")
