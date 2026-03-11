def cyclic_shift(lst, k):
    n = len(lst)
    if n == 0:
        return lst
    
    # если k больше длины списка
    k = k % n
    
    if k == 0:
        return lst
    return lst[-k:] + lst[:-k]

lst = [1, 2, 3, 4, 5]
k = int(input("Сдвиг: "))

shifted = cyclic_shift(lst, k)

print(f"Изначальный список: {lst}")
print(f"Сдвинутый список: {shifted}")
