def calculate_average(arr):
    if len(arr) == 0:
        return 0

    total_sum = 0
    count = 0

    for number in arr:
        total_sum += number
        count += 1

    average = total_sum / count
    return average


numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"Среднее арифметическое: {average}")
