class Game:
    Choices_database = {
        1: ('Камень', 'Бумага'),
        2: ('Ножницы', 'Камень'),
        3: ('Бумага', 'Ножницы')
    }

    def __init__(self, choice_number):
        self.choice_number = choice_number
        self.choice_name = self.Choices_database[choice_number][0]
        self.loses_to = self.Choices_database[choice_number][1]

    def __str__(self):
        return self.choice_name

    def is_losing_to(self, other_choice):
        return self.loses_to == other_choice.choice_name.lower()


class ClassDlyaIgrokov:
    def __init__(self, participant_name):
        self.name = participant_name
        self.total_score = 0
        self.currect_choice = None

    def increase_score(self):
        self.total_score += 1

    def reset_score(self):
        self.total_score = 0


class Igrok(ClassDlyaIgrokov):
    def make_choice(self):
        print(f"\n{self.name}, твой ход! Выбери:")
        print("1 - камень")
        print("2 - ножницы")
        print("3 - бумага")
        while True:
            try:
                user_input = int(input())
                if 1 <= user_input <= 3:
                    self.currect_choice = Game(user_input)
                    print("\n" * 2)
                    return self.currect_choice
                else:
                    print("Ошибка! Необходимо ввести цифру от 1 до 3.")
            except ValueError:
                print("Ошибка! Введите целое число.")


class Round:
    def __init__(self, first, second, number):
        self.first_player = first
        self.second_player = second
        self.round_id = number
        self.round_winner = None

    def execute(self):
        print(f"\nХод {self.first_player.name}")
        first_player_choice = self.first_player.make_choice()

        print(f"\nХод {self.second_player.name}")
        second_player_choice = self.second_player.make_choice()

        print(f"{self.first_player.name} показал: {first_player_choice}")
        print(f"{self.second_player.name} показал: {second_player_choice}")

        self.round_winner = self.determine_round_winner(first_player_choice, second_player_choice)

        if self.round_winner is None:
            print("Ничья")
        else:
            print(f"{self.round_winner.name} выигрывает раунд!")
            self.round_winner.increase_score()

    def determine_round_winner(self, one, two):
        if one.choice_number == two.choice_number:
            return None
        if two.is_losing_to(one):
            return self.first_player
        else:
            return self.second_player


class GameSession:
    def __init__(self, one, two, number_of_rounds):
        self.one = one
        self.two = two
        self.total_rounds = number_of_rounds
        self.completed_rounds = 0

    def start_game(self):
        for i in range(1, self.total_rounds + 1):
            print(f"\n--- Раунд {i} ---")
            current_round = Round(self.one, self.two, i)
            current_round.execute()
            self.completed_rounds += 1
        self.show_results()

    def show_results(self):
        score_one = self.one.total_score
        score_two = self.two.total_score
        print(f"\nСчет:\n{self.one.name}: {score_one}\n{self.two.name}: {score_two}")

        if score_one > score_two:
            print(f"Победил {self.one.name}!")
        elif score_two > score_one:
            print(f"Победил {self.two.name}!")
        else:
            print("Ничья по итогам игры!")

    def reset_game(self):
        self.completed_rounds = 0
        self.one.reset_score()
        self.two.reset_score()


def run_game():
    name_one = input("Введите имя первого игрока: ")
    name_two = input("Введите имя второго игрока: ")

    first_player = Igrok(name_one)
    second_player = Igrok(name_two)

    while True:
        game = GameSession(first_player, second_player, number_of_rounds=3)
        game.start_game()

        answer = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if answer == 'нет':
            print(":(")
            break
        else:
            game.reset_game()


if __name__ == "__main__":
    run_game()
