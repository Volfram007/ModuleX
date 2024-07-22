import unittest
from taskFiles import runner_and_tournament as tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = tournament.Runner('Усэйн', 10)
        self.runner2 = tournament.Runner('Андрей', 9)
        self.runner3 = tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print({place: runner.name for place, runner in i.items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament1(self):
        t = tournament.Tournament(90, self.runner1, self.runner3)
        result = t.start()
        TournamentTest.all_results.append(result)
        # Проверка наличия в списке items результатов последнего слова "Ник"
        # res = True if "Ник" == next(reversed(result.values())) else False
        res = "Ник" == next(reversed(result.values()))
        self.assertTrue(res, f"Получен: {next(reversed(result.values()))}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament2(self):
        t = tournament.Tournament(90, self.runner2, self.runner3)
        result = t.start()
        TournamentTest.all_results.append(result)
        res = "Ник" == next(reversed(result.values()))
        self.assertTrue(res, f"Получен: {next(reversed(result.values()))}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament3(self):
        t = tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = t.start()
        TournamentTest.all_results.append(result)
        res = "Ник" == next(reversed(result.values()))
        self.assertTrue(res, f"Получен: {next(reversed(result.values()))}")


if __name__ == '__main__':
    unittest.main()
