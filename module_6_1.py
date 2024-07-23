class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            Animal.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            Animal.alive = False

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

# Создание объектов классов и выполнение действий
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

print(Animal.alive)  # True
print(Animal.fed)    # False
a1.eat(p1)           # Волк с Уолл-Стрит не стал есть Цветик семицветик
print(Animal.alive)  # False
a2.eat(p2)           # Хатико съел Заводной апельсин
print(Animal.fed)    # True

