def caesar_cipher(text, shift):
    lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    
    result = []
    for char in text:
        if char in lower:
            result.append(lower[(lower.index(char) + shift) % len(lower)])
        elif char in upper:
            result.append(upper[(upper.index(char) + shift) % len(upper)])
        else:
            result.append(char)
    
    return ''.join(result)

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

# Шифруем и выводим
encrypted = caesar_cipher(message, shift)
print(f"Зашифрованное сообщение: {encrypted}")
