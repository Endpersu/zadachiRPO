def count_vowels(input_string):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count


user_input = input("Введите строку: ")
vowel_count = count_vowels(user_input)
print(f"Количество гласных букв в строке: {vowel_count}")
