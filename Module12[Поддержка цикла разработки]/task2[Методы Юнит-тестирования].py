import unittest
from taskFiles import runner_and_tournament as tournament


class TournamentTest(unittest.TestCase):
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

    def test_Tournament1(self):
        t = tournament.Tournament(90, self.runner1, self.runner3)
        result = t.start()
        TournamentTest.all_results.append(result)
        # Проверка наличия в списке items результатов последнего слова "Ник"
        # res = True if "Ник" == next(reversed(result.values())) else False
        res = "Ник" == next(reversed(result.values()))
        self.assertTrue(res, f"Получен: {next(reversed(result.values()))}")

    def test_Tournament2(self):
        t = tournament.Tournament(90, self.runner2, self.runner3)
        result = t.start()
        TournamentTest.all_results.append(result)
        res = "Ник" == next(reversed(result.values()))
        self.assertTrue(res, f"Получен: {next(reversed(result.values()))}")

    def test_Tournament3(self):
        t = tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = t.start()
        TournamentTest.all_results.append(result)
        res = "Ник" == next(reversed(result.values()))
        self.assertTrue(res, f"Получен: {next(reversed(result.values()))}")


if __name__ == '__main__':
    unittest.main()

# **Задача "Методы Юнит-тестирования"**
#
# 1. Скачайте исходный код с GitHub.
# 2. Изучите изменения в классе `Runner` и новый класс `Tournament`.
#     - У `Runner` появился атрибут `speed`, метод `__eq__`, и изменены методы `run` и `walk`.
#     - `Tournament` включает дистанцию, список участников и метод `start`.
#
# 3. Создайте класс `TournamentTest`, наследуемый от `TestCase` из модуля `unittest`.
# 4. Реализуйте следующие методы в `TournamentTest`:
#     - `setUpClass`: создаёт атрибут `all_results`, который сохраняет результаты всех тестов.
#     - `setUp`: создаёт три объекта `Runner`:
#         - Усэйн (скорость 10)
#         - Андрей (скорость 9)
#         - Ник (скорость 3)
#     - `tearDownClass`: выводит `all_results`.
#
# 5. Напишите методы тестирования забегов:
#     - Для каждого метода создайте объект `Tournament` на дистанцию 90, запустите метод `start`, сохраните результат
#     в `results`, используйте `assertTrue`, чтобы проверить, что последний объект в `results` - Ник.
#     - Тесты должны проверять:
#         - Усэйн и Ник
#         - Андрей и Ник
#         - Усэйн, Андрей и Ник
#
# **Дополнительно (не обязательно):**
# Попробуйте исправить логическую ошибку в методе `start` класса `Tournament`.
#
# **Пример вывода:**
# ```
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Усэйн, 2: Андрей, 3: Ник}
#
# Ran 3 tests in 0.001s
# OK
# ```
