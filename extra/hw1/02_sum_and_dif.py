def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def count_digits(n):
    return len(str(n))

number = int(input("Введите число: "))

sum_digits = sum_of_digits(number)
count = count_digits(number)
difference = sum_digits - count

print(f"Сумма чисел: {sum_digits}")
print(f"Количество цифр в числе: {count}")
print(f"Разность суммы и количества цифр: {difference}")
