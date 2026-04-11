def schitalka(n, k):
    if n == 1:
        return 1
    return (schitalka(n - 1, k) + k - 1) % n + 1

n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))

result = schitalka(n, k)
print(f"\nОстался человек под номером {result}")
