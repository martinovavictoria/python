n = int(input("Количество видеокарт: "))
old_list = []

for i in range(1, n + 1):
    card = int(input(f"{i} Видеокарта: "))
    old_list.append(card)

max_generation = max(old_list)

new_list = []
for card in old_list:
    if card != max_generation:
        new_list.append(card)

print(f"Старый список видеокарт: {old_list}")
print(f"Новый список видеокарт: {new_list}")
