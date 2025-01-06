import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class Tournament:
    def __init__(self, distance, *runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        for runner in self.runners:
            time = self.distance / runner.speed
            results[time] = runner.name
        return results

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(f"{key}: {cls.all_results[key]}")

    def test_race_usain_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_andrey_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == "__main__":
    unittest.main()
