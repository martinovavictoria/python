'''Это декоратор с параметрами, который кеширует результаты вызовов функций. Если функция вызывается с теми же аргументами повторно, результат берётся из кеша, а не вычисляется заново. Кеш может сохраняться в JSON-файл между запусками программы.

Декоратор cache(file_name=None, key_type='args')
Это функция, возвращающая декоратор. Такая конструкция позволяет передавать параметры (file_name и key_type) в декоратор.

Внутреннее хранилище кеша
cache_storage = {}
Словарь, где ключ - это набор аргументов, а значение — результат функции.'''

import json
import os
import ast

def cache(file_name=None, key_type='args'):
    def decorator(func):
        cache_storage = {}
        #Загрузка кеша из файла (при наличии)
        if file_name and os.path.exists(file_name):
            try:
                with open(file_name, 'r') as f:
                    saved_cache = json.load(f)
                    for str_key, value in saved_cache.items():
                        original_key = ast.literal_eval(str_key)
                        cache_storage[original_key] = value
                    print(f"Загружено {len(cache_storage)} записей из {file_name}")
            except:
                pass
        #Функция формирования ключа, создаёт уникальный ключ для кеша:'args' - учитывает только позиционные аргументы, 'kwargs' - учитывает только именованные аргументы, 'both' - учитывает и те, и другие
        def make_key(*args, **kwargs):
            if key_type == 'args':
                return (func.__name__,) + args
            elif key_type == 'kwargs':
                return (func.__name__,) + tuple(sorted(kwargs.items()))
            elif key_type == 'both':
                return (func.__name__, args, tuple(sorted(kwargs.items())))
            else:
                return (func.__name__,) + args
        
        def save_cache():
            if file_name:
                try:
                    serializable = {}
                    for key, value in cache_storage.items():
                        serializable[str(key)] = value  # Ключ-кортеж → строка
                    with open(file_name, 'w') as f:
                        json.dump(serializable, f)
                except:
                    pass
        
        def wrapper(*args, **kwargs):
            key = make_key(*args, **kwargs)
            
            if key in cache_storage:
                print(f"{func.__name__}{args} взято из кеша: {cache_storage[key]}")
                return cache_storage[key]
            
            print(f"Вычисляем {func.__name__}{args}")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            save_cache()
            return result
        
        return wrapper
    return decorator



@cache(file_name='sum_cache.json', key_type='args')
def calculate_sum(*numbers):
    return sum(numbers)

@cache(file_name='multiply_cache.json', key_type='both')
def calculate_multiply(*numbers, factor=1):
    result = 1
    for n in numbers:
        result *= n
    return result * factor

print(calculate_sum(2, 3))
print(calculate_sum(2, 3))
print(calculate_multiply(2, 3, factor=2))
print(calculate_multiply(2, 3, factor=2))
