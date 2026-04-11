n = int(input("Кол-во чисел: "))
numbers = []
for i in range(n):
    num = int(input("Число: "))
    numbers.append(num)

print(f"\nПоследовательность: {numbers}")

def is_palindrome(arr):
    return arr == arr[::-1]

# Ищем минимальное количество чисел для добавления
found = False
for i in range(n + 1):
    # Проверяем, станет ли последовательность палиндромом, если добавить первые i чисел в обратном порядке
    test_seq = numbers + numbers[:i][::-1]
    if is_palindrome(test_seq):
        to_add = numbers[:i][::-1]
        print(f"Нужно приписать чисел: {len(to_add)}")
        print(f"Сами числа: {to_add}")
        found = True
        break

if not found:
    print("Нужно приписать чисел: 0")
    print("Сами числа: []")
