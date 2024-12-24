a1 = int(input("Введите число единиц: "))
a2 = int(input("Введите число десяток: "))
a3 = int(input("Введите число сотен: "))
b1 = int(input("Введите число единиц: "))
b2 = int(input("Введите число десяток: "))

sum_units = (a1 + b1) % 10
sum_tens = (a2 + b2 + (a1 + b1) // 10) % 10
sum_hundreds = a3 + (a2 + b2 + (a1 + b1) // 10) // 10

result = (sum_hundreds, sum_tens, sum_units)
print(result)