class Animal:
    def __init__(self):
        pass

class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx

class Eagle(Animal):
    def __init__(self):
        super().__init__()
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        self.sound = 'I train, eat, sleep, and repeat'

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

# Пример использования
p1 = Pegasus()

print(p1.get_pos())  # (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)

p1.voice()  # I train, eat, sleep, and repeat
