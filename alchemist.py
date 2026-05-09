class Element:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class AlchemyGame:
    def __init__(self):
        # Словарь открытых элементов: имя -> объект Element
        self.elements = {}
        # Словарь рецептов: (имя1, имя2) -> имя_результата
        self.recipes = {}

        # Добавляем 4 базовых элемента
        self.elements["Огонь"] = Element("Огонь")
        self.elements["Вода"] = Element("Вода")
        self.elements["Земля"] = Element("Земля")
        self.elements["Воздух"] = Element("Воздух")
      
        self._create_recipes()

    def _create_recipes(self):
        self._add_recipe("Огонь", "Вода", "Пар")
        self._add_recipe("Огонь", "Земля", "Лава")
        self._add_recipe("Огонь", "Воздух", "Энергия")
        self._add_recipe("Вода", "Земля", "Грязь")
        self._add_recipe("Вода", "Воздух", "Дождь")
        self._add_recipe("Земля", "Воздух", "Пыль")
        self._add_recipe("Лава", "Вода", "Камень")
        self._add_recipe("Грязь", "Огонь", "Кирпич")
        self._add_recipe("Энергия", "Воздух", "Буря")
        self._add_recipe("Энергия", "Грязь", "Жизнь")
        self._add_recipe("Пыль", "Огонь", "Стекло")
        self._add_recipe("Кирпич", "Огонь", "Печь")
        self._add_recipe("Камень", "Огонь", "Металл")
        self._add_recipe("Жизнь", "Вода", "Водоросли")
        self._add_recipe("Жизнь", "Земля", "Растение")
        self._add_recipe("Буря", "Вода", "Цунами")

    def _add_recipe(self, elem1_name, elem2_name, result_name)
        key = tuple(sorted([elem1_name, elem2_name]))
        self.recipes[key] = result_name

    def combine(self, name1, name2):
        if name1 not in self.elements:
            print("Ошибка: элемент '" + name1 + "' ещё не открыт.")
            return None
        if name2 not in self.elements:
            print("Ошибка: элемент '" + name2 + "' ещё не открыт.")
            return None
        if name1 == name2:
            print("Смешивание " + name1 + " с самим собой ничего не даёт.")
            return None

        key = tuple(sorted([name1, name2]))
        if key in self.recipes:
            result_name = self.recipes[key]
            if result_name in self.elements:
                print("Этот элемент уже открыт: " + result_name + ".")
                return result_name
            else:
                self.elements[result_name] = Element(result_name)
                print("Открыт новый элемент: " + result_name + "!")
                return result_name
        else:
            print("Смешивание " + name1 + " и " + name2 + " ничего не даёт.")
            return None

    def show_elements(self):
        print("--- Открытые элементы ---")
        # Проходим по словарю и выводим каждый элемент
        for name in self.elements:
            print(" - " + name)
        print("Всего открыто: " + str(len(self.elements)) + " элементов.")
        print()

    def show_recipes(self):
        print("--- Все рецепты ---")
        for key in self.recipes:
            elem1 = key[0]
            elem2 = key[1]
            result = self.recipes[key]
            print(elem1 + " + " + elem2 + " = " + result)
        print()
      
game = AlchemyGame()

# Показываем начальные элементы
print("Исходные элементы:")
game.show_elements()

# Пробуем смешивать
game.combine("Огонь", "Вода")     # Пар
game.combine("Огонь", "Земля")    # Лава
game.combine("Лава", "Вода")      # Камень
game.combine("Вода", "Земля")     # Грязь
game.combine("Грязь", "Огонь")    # Кирпич
game.combine("Энергия", "Грязь")  # Жизнь
game.combine("Жизнь", "Земля")    # Растение
game.combine("Камень", "Огонь")   # Металл

# Пробуем несуществующую комбинации
game.combine("Пар", "Камень")  
game.combine("Огонь", "Огонь")   

print()
game.show_elements()
