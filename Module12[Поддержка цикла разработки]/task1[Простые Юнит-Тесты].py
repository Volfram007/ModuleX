import unittest
import runner as run_


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = run_.Runner("Name1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = run_.Runner("Name2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = run_.Runner("Name1")
        runner2 = run_.Runner("Name2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()

# Создайте класс RunnerTest, наследуемый от TestCase из модуля unittest.
# Напишите следующие методы в классе RunnerTest:
# test_walk: создайте объект класса Runner, вызовите метод walk 10 раз,
# проверьте, что distance равно 50 с помощью assertEqual.
# test_run: создайте объект класса Runner, вызовите метод run 10 раз, проверьте,
# что distance равно 100 с помощью assertEqual.
# test_challenge: создайте 2 объекта класса Runner, вызовите метод run для одного объекта и
# метод walk для другого 10 раз, проверьте, что их distance не равны с помощью assertNotEqual.
# Запустите тесты и убедитесь, что все они проходят.
