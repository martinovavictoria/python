skates_count = int(input("Кол-во коньков: "))
skates = []
for i in range(1, skates_count + 1):
    size = int(input(f"Размер {i}-й пары: "))
    skates.append(size)

people_count = int(input("\nКол-во людей: "))
feet = []
for i in range(1, people_count + 1):
    size = int(input(f"Размер ноги {i}-го человека: "))
    feet.append(size)

skates.sort()
feet.sort()

# Подбираем ролики (удаляем использованные)
people_with_skates = 0
for foot in feet:
    for i, skate in enumerate(skates):
        if skate >= foot:
            people_with_skates += 1
            skates.pop(i)
            break

print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {people_with_skates}")
