def smallest_divisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n  # если делителей не найдено, число простое

n = int(input("Введите число: "))
result = smallest_divisor(n)

print(f"Наименьший делитель, отличный от единицы: {result}")
