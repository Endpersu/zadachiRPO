def find_x(target):
    for first_digit in range(1, 10):
        for last_two_digits in range(0, 100):
            if first_digit * 10 + last_two_digits * 10 + first_digit == target:
                return first_digit * 100 + last_two_digits
    return None


result = find_x(564)
print(result)