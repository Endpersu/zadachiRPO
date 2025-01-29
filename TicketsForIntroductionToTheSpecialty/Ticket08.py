def remove_duplicates(arr):
    unique_elements = set(arr)
    return list(unique_elements)


array_with_duplicates = [1, 2, 3, 2, 4, 5, 5, 6, 1, 7]
print(f"Исходный массив: {array_with_duplicates}")


result_array = remove_duplicates(array_with_duplicates)
print(f"Массив без дубликатов: {result_array}")
