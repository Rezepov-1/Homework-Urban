import unittest
from runner import Runner
from tournament import Tournament

# Определение декоратора перед использованием
def check_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Контроль выполнения тестов

    @check_frozen
    def test_walk(self):
        runner = Runner("John", 10)
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @check_frozen
    def test_run(self):
        runner = Runner("Jane", 10)
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @check_frozen
    def test_challenge(self):
        runner1 = Runner("Alice", 10)
        runner2 = Runner("Bob", 5)
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Контроль выполнения тестов

    @check_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, [Runner("Усэйн", 10), Runner("Ник", 3)])
        result = tournament.start()
        self.assertTrue(result[max(result)] == "Ник")

    @check_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, [Runner("Андрей", 9), Runner("Ник", 3)])
        result = tournament.start()
        self.assertTrue(result[max(result)] == "Ник")

    @check_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, [Runner("Усэйн", 10), Runner("Андрей", 9), Runner("Ник", 3)])
        result = tournament.start()
        self.assertTrue(result[max(result)] == "Ник")