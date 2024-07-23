class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.current_floor = 1  # Добавляем текущий этаж

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(self.current_floor, new_floor + 1):
                print(floor)
            self.current_floor = new_floor  # Обновляем текущий этаж
        else:
            print("Такого этажа не существует")

    def add_floor(self):
        self.number_of_floors += 1
        print(f"Этаж добавлен. Теперь в здании {self.number_of_floors} этажей.")

    def remove_floor(self):
        if self.number_of_floors > 1:
            self.number_of_floors -= 1
            print(f"Этаж удален. Теперь в здании {self.number_of_floors} этажей.")
        else:
            print("Невозможно удалить последний этаж.")

    def get_current_floor(self):
        return self.current_floor

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}, текущий этаж: {self.current_floor}"

# Создание объектов класса House
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)