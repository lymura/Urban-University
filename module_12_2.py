class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        participants = list(self.participants)

        while participants:
            for participant in participants:
                remaining_distance = self.full_distance - participant.distance
                steps_to_finish = max(remaining_distance // participant.speed, 1)
                participant.distance += participant.speed * steps_to_finish

                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    participants.remove(participant)

        return finishers


import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        # Создаем трех бегунов
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

    def tearDownClass(cls):
        # Выводим все результаты после завершения всех тестов
        for key, value in cls.all_results.items():
            print(value)

    def test_usain_vs_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.assertEqual(results[max(results)], "Ник")
        self.__class__.all_results[self._testMethodName] = results

    def test_andrey_vs_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.assertEqual(results[max(results)], "Ник")
        self.__class__.all_results[self._testMethodName] = results

    def test_all_three(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.assertEqual(results[max(results)], "Ник")
        self.__class__.all_results[self._testMethodName] = results


if __name__ == '__main__':
    unittest.main()


def test_equal_speed(self):
    equal_runner_1 = Runner("Равный1", speed=8)
    equal_runner_2 = Runner("Равный2", speed=8)
    tournament = Tournament(80, equal_runner_1, equal_runner_2)
    results = tournament.start()
    self.assertIn(equal_runner_1, results.values())
    self.assertIn(equal_runner_2, results.values())
    self.__class__.all_results[self._testMethodName] = results


def test_complex_case(self):
    complex_runner_1 = Runner("Сложный1", speed=7)
    complex_runner_2 = Runner("Сложный2", speed=6)
    complex_runner_3 = Runner("Сложный3", speed=4)
    tournament = Tournament(120, complex_runner_1, complex_runner_2, complex_runner_3)
    results = tournament.start()
    self.assertEqual(len(results), 3)
    self.assertNotEqual(results[1], complex_runner_3)
    self.assertNotEqual(results[2], complex_runner_3)
    self.__class__.all_results[self._testMethodName] = results