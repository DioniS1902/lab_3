from ..all_animals import *
from ..manager import *


class Test:
    def __init__(self):
        self.savana = SavannaManager()
        self.savana.add_animals([Pinguin(random.randrange(5, 20), random.randrange(5, 20)) for i in range(5)])
        self.savana.add_animals([Bear(random.randrange(5, 20), random.randrange(5, 20)) for i in range(5)])
        self.savana.add_animals([Cod(random.randrange(5, 20), random.randrange(5, 20)) for i in range(5)])
        self.savana.add_animals([Seals(random.randrange(5, 20), random.randrange(5, 20)) for i in range(5)])

    def test_print(self):
        print("Тест виводу")
        [print(animal) for animal in self.savana.animals]

    def test_sort(self):
        animals = self.savana.find_predators(10)
        sorted_animals = self.savana.sort_by_weight_of_food_consumed(animals, SortOrder.ASC)
        print("\nТест сортування")
        [print(animal) for animal in sorted_animals]

        reverse_sorted_animals = self.savana.sort_by_weight_of_food_consumed(animals, SortOrder.DESC)
        print("\nЗворотний тест сортування")
        [print(animal) for animal in reverse_sorted_animals]
