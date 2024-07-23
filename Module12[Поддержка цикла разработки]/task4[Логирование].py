import logging
import unittest
from taskFiles import rt_with_exceptions as rt

# Настройка логирования
logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    filemode='w',  # Используйте 'w' для записи в новый файл
    format='%(asctime)s | %(levelname)s: %(message)s',
    encoding='utf-8'
)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner = rt.Runner("Name1",-5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = rt.Runner(132)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = rt.Runner("Name1")
        runner2 = rt.Runner("Name2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()

# **Задача "Логирование бегунов"**
# - Класс `Runner` теперь выбрасывает исключения, если передан неверный тип в `name` или
# отрицательное значение в `speed`.
#
# **Настройка логирования:**
# 1. В модуле `tests_12_4.py`:
#     - Импортируйте пакет `logging`.
#     - Настройте `basicConfig`:
#         - Уровень: `INFO`
#         - Режим: `чтение`
#         - Название файла: `runner_tests.log`
#         - Кодировка: `UTF-8`
#         - Формат вывода: обязательная информация: уровень логирования, сообщение логирования.
#
# **Обновите методы тестирования в классе `RunnerTest`:**
# - `test_walk`:
#     - Оберните основной код конструкцией `try-except`.
#     - При создании объекта `Runner` передавайте отрицательное значение в `speed`.
#     - В блоке `try`:
#         - Логируйте сообщение `INFO`: '"test_walk" выполнен успешно'.
#     - В блоке `except`:
#         - Обработайте исключение и логируйте его на уровне `WARNING` с сообщением "Неверная скорость для Runner".
# - `test_run`:
#     - Оберните основной код конструкцией `try-except`.
#     - При создании объекта `Runner` передавайте значение не строкового типа в `name`.
#     - В блоке `try`:
#         - Логируйте сообщение `INFO`: '"test_run" выполнен успешно'.
#     - В блоке `except`:
#         - Обработайте исключение и логируйте его на уровне `WARNING` с сообщением
#         "Неверный тип данных для объекта Runner".
