def factorial_recursive(N):
    if N == 0:
        return 1
    else:
        return N * factorial_recursive(N - 1)


N = int(input("Введите неотрицательное целое число N: "))


result = factorial_recursive(N)
print(f"Факториал числа {N} равен {result}.")
