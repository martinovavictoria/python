import random

team1 = []
team2 = []

for _ in range(20):
    team1.append(round(random.uniform(5, 10), 2))
    team2.append(round(random.uniform(5, 10), 2))

winners = []
for i in range(20):
    winners.append(max(team1[i], team2[i]))

print(f"Первая команда: {team1}")
print(f"Вторая команда: {team2}")
print(f"Победители тура: {winners}")
