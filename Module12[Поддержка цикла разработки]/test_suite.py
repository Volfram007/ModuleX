import unittest
import test_runner
import test_tournament

test_suite = unittest.TestSuite()
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_tournament.TournamentTest))

runner_test = unittest.TextTestRunner(verbosity=2)
runner_test.run(test_suite)

# **Задача "Заморозка кейсов"**
# Используйте те же `TestCase`, что и в предыдущем задании: `RunnerTest` и `TournamentTest`.
#
# **Часть 1. TestSuite:**
# 1. Создайте модуль `suite_12_3.py`.
# 2. Опишите объект `TestSuite` и сохраните его в переменную.
# 3. Добавьте тесты `RunnerTest` и `TournamentTest` в этот `TestSuite`.
# 4. Создайте объект класса `TextTestRunner` с аргументом `verbosity=2`.
#
# **Часть 2. Пропуск тестов:**
# 1. Добавьте атрибут `is_frozen = False` к `RunnerTest` и `is_frozen = True` к `TournamentTest`.
# 2. Напишите декоратор для каждого метода (кроме @classmethod), который:
#     - Выполняет тесты при `is_frozen = False`.
#     - Пропускает тесты и выводит сообщение "Тесты в этом кейсе заморожены" при `is_frozen = True`.
#
# **Запуск:**
# 1. Запустите `TestSuite`.
# 2. Проверьте результаты тестов из обоих `TestCase`.
#
# **Пример вывода:**
# ```
# test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
# test_run (tests_12_3.RunnerTest.test_run) ... ok
# test_walk (tests_12_3.RunnerTest.test_walk) ... ok
# test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s
#
# OK (skipped=3)
# ```