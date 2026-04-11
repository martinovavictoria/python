def merge_sorted_lists(list1, list2):
    """Объединяет два отсортированных списка в один без дубликатов"""
    merged = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not merged or list2[j] != merged[-1]:
                merged.append(list2[j])
            j += 1
        else:  # list1[i] == list2[j]
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
            j += 1
    
    while i < len(list1):
        if not merged or list1[i] != merged[-1]:
            merged.append(list1[i])
        i += 1
    
    while j < len(list2):
        if not merged or list2[j] != merged[-1]:
            merged.append(list2[j])
        j += 1
    
    return merged


# Тестирование
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)


# Тест 1: Обычный случай
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]

# Тест 2: С дубликатами
print(merge_sorted_lists([1, 2, 2, 3], [2, 3, 4, 4]))  # [1, 2, 3, 4]

# Тест 3: Пустые списки
print(merge_sorted_lists([], [1, 2, 3]))  # [1, 2, 3]
print(merge_sorted_lists([1, 2, 3], []))  # [1, 2, 3]
print(merge_sorted_lists([], []))  # []

# Тест 4: Один список короче другого
print(merge_sorted_lists([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Тест 5: Все элементы одинаковые
print(merge_sorted_lists([5, 5, 5], [5, 5]))  # [5]

# Тест 6: Отрицательные числа
print(merge_sorted_lists([-5, -3, 0, 2], [-4, -2, 1, 3]))  # [-5, -4, -3, -2, 0, 1, 2, 3]
