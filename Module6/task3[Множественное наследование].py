class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

'''
### Задача "Мифическое наследование"
Напишите три класса: `Horse`, `Eagle` и `Pegasus`.

#### Класс Horse:
Атрибуты:
- `x_distance = 0` — пройденный путь.
- `sound = 'Frrr'` — звук лошади.

Методы:
- `run(self, dx)` — увеличивает `x_distance` на `dx`.

#### Класс Eagle:
Атрибуты:
- `y_distance = 0` — высота полёта.
- `sound = 'I train, eat, sleep, and repeat'` — звук орла.

Методы:
- `fly(self, dy)` — увеличивает `y_distance` на `dy`.

#### Класс Pegasus (наследник Horse и Eagle):
Атрибуты:
- Наследует атрибуты от `Horse` и `Eagle`.

Методы:
- `move(self, dx, dy)` — вызывает методы `run` и `fly` с параметрами `dx` и `dy`.
- `get_pos(self)` — возвращает кортеж `(x_distance, y_distance)`.
- `voice(self)` — выводит значение атрибута `sound`.

#### Пункты задачи:
1. Создайте классы `Horse` и `Eagle` с указанными атрибутами и методами.
2. Создайте класс `Pegasus` с указанными атрибутами и методами.
3. Создайте объект класса `Pegasus` и проверьте работу всех методов.

Пример выполнения программы:
```python
p1 = Pegasus()

print(p1.get_pos())    # (0, 0)
p1.move(10, 15)
print(p1.get_pos())    # (10, 15)
p1.move(-5, 20)
print(p1.get_pos())    # (5, 35)

p1.voice()             # I train, eat, sleep, and repeat
```

### Примечания:
- Будьте внимательны при множественном наследовании и использовании `super()`.
- Порядок наследования влияет на значение унаследованных атрибутов.
'''
