text = input("Введите текст: ")

vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

vowels_list = [char for char in text if char in vowels]

print(f"Список гласных букв: {vowels_list}")
print(f"Длина списка: {len(vowels_list)}")
