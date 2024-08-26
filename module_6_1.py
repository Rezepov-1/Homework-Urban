# Создайте:
# 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
# name - индивидуальное название каждого животного.
# Для класса Plant атрибут edible = False(съедобность),
# name - индивидуальное название каждого растения
#
# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.
#
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
#
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
# меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
# меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
#
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Plant:
    edible = False  # Атрибут класса (определённый для всех растений)

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)  # Наследуем конструктор Animal

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)  # Наследуем конструктор Animal

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


# Создание объектов и тестирование
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

print(a1.alive)  # True
print(a2.fed)  # False
a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Хатико съел Заводной апельсин
print(a1.alive)  # False
print(a2.fed)  # True