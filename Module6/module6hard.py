# Наследование классов
from math import pi, sqrt


class Figure:  # Базовый класс для геометрических фигур
    sides_count = 0

    def __init__(self, color, *sides):
        # Проверка цвета, если он корректный, иначе устанавливается черный
        self._color = color if self.is_valid_color(*color) else (0, 0, 0)

        # Проверка и установка сторон, если они корректные, иначе создается список единиц
        self._sides = list(sides) if self.is_valid_sides(*sides) else [1] * self.sides_count

        self.filled = False

    # Получения цвета фигуры
    def get_color(self):
        return self._color

    # Проверки корректности цвета
    def is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    # Установки цвета фигуры
    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self._color = (r, g, b)
        # else:
        #     print("Неверный цвет фигуры RGB {} {} {}".format(r, g, b))

    # Получения списка сторон фигуры
    def get_sides(self):
        return self._sides

    # Проверки корректности сторон фигуры
    def is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(x, int) and x > 0 for x in sides)

    # Установки новых сторон фигуры
    def set_sides(self, *sides):
        if self.is_valid_sides(*sides) and len(sides):
            self._sides = list(sides)
        # else:
        #     print("Неверное количество сторон фигуры {}, нужно {}".format(len(sides), self.sides_count))

    # Магический метод для получения периметра фигуры
    def __len__(self):
        return sum(self._sides)


class Circle(Figure):
    # Количество сторон круга
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    # Получения площади круга через его длину
    def get_square(self):
        # Вычисление радиуса круга через его длину
        _radius = self.get_sides()[0] / (2 * pi)
        return pi * (_radius ** 2)


class Triangle(Figure):
    # Количество сторон треугольника
    sides_count = 3

    def __init__(self, color, *sides):
        # Создание списка из 3 одинаковых сторон
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        # Вызов конструктора класса Figure
        super().__init__(color, *sides)
        # Вычисление высоты треугольника
        self._height = self.calc_height()

    # Вычисления высоты треугольника
    def calc_height(self):
        a, b, c = self.get_sides()  # Получение сторон треугольника
        p = (a + b + c) / 2  # Полупериметр треугольника
        return 2 * sqrt(p * (p - a) * (p - b) * (p - c)) / a  # Формула Герона

    # Получения площади треугольника
    def get_square(self):
        return 0.5 * self.get_sides()[0] * self._height


class Cube(Figure):
    # Количество сторон куба
    sides_count = 12

    def __init__(self, color, *sides):
        # Создание списка из 12 одинаковых сторон
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        # Вызов конструктора класса Figure
        super().__init__(color, *sides)

    # Получения объема куба
    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # Создание круга
cube1 = Cube((222, 35, 130), 6)  # Создание куба

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменение цвета круга
cube1.set_color(300, 70, 15)  # Попытка изменить цвет куба (не изменится, т.к. некорректный цвет)
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Попытка изменить стороны куба (не изменится, т.к. некорректное количество)
circle1.set_sides(15)  # Изменение стороны (длины окружности) круга
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216

# Проверка
print('\n\tТест треугольник: ')
triangle1 = Triangle((0, 0, 0), 10)
print('Стороны1:', triangle1.get_sides())
triangle1 = Triangle((200, 200, 100), 10, 6)
print('Стороны2:', triangle1.get_sides())
triangle1 = Triangle((200, 200, 100), 10)
print('Площадь {}:'.format(triangle1.get_sides()), triangle1.get_square())
print('\tТест круг: ')
circle1 = Circle((200, 200, 100), 66)
print('Длина1:', circle1.get_sides())
circle1 = Circle((200, 200, 100), 66, 15)
print('Длина2:', circle1.get_sides())
circle1 = Circle((200, 200, 100), 66)
print('Площадь {}:'.format(circle1.get_sides()), circle1.get_square())
print('\tТест куб: ')
cube1 = Cube((200, 200, 100), 9)
print('Стороны1:', cube1.get_sides())
cube1 = Cube((200, 200, 100), 9, 12)
print('Стороны2:', cube1.get_sides())
cube1 = Cube((200, 200, 100), 66)
print('Объём [{},..]:'.format(cube1.get_sides()[0]), cube1.get_volume())
