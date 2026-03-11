results = list(map(int, input("Введите результаты экспериментов: ").split()))

print("Чётные числа в обратном порядке:")

# Перебираем список с конца
for i in range(len(results) - 1, -1, -1):
    if results[i] % 2 == 0:
        print(results[i], end=" ")
