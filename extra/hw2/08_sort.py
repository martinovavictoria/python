#быстаря сортировка O(n log n)
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

lst = [1, 4, -3, 0, 10]
print(f"Изначальный список: {lst}")
quick_sort(lst, 0, len(lst) - 1)
print(f"Отсортированный список: {lst}")

#сортировка пузырьком, в случае если чисел немного тоже быстрая O(n²)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Обмен элементов
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

lst = [1, 4, -3, 0, 10]
print(f"Изначальный список: {lst}")
sorted_lst = bubble_sort(lst)
print(f"Отсортированный список: {sorted_lst}")
