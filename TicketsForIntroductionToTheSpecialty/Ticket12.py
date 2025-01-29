def is_palindrome(s):
    cleaned_s = ''.join(s.split()).lower()
    return cleaned_s == cleaned_s[::-1]


str1 = input("Введите строку: ")
str2 = input("Введите строку: ")

print(is_palindrome(str1))
print(is_palindrome(str2))
