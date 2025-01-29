def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


array = [5, 3, 8, 4, 2]
target_element = 8

result = linear_search(array, target_element)

if result != -1:
    print(f'Элемент {target_element} найден на индексе {result}.')
else:
    print(f'Элемент {target_element} не найден в массиве.')
