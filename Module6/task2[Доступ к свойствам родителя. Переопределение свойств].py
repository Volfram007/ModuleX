class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}\n")

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Невозможно покрасить в {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Количество пассажиров

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Изначальные свойства
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

# Меняем свойства
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()

'''
### Задача "Изменять нельзя получать"
Создайте два класса: `Vehicle` и `Sedan`, где `Vehicle` — это любой транспорт, а `Sedan` — наследник класса `Vehicle`.

#### Класс Vehicle:
Атрибуты объекта:
- `owner` (str) — владелец транспорта (может меняться).
- `__model` (str) — модель транспорта (неизменяемый).
- `__engine_power` (int) — мощность двигателя (неизменяемая).
- `__color` (str) — цвет транспорта (неизменяемый).

Атрибут класса:
- `__COLOR_VARIANTS` — список допустимых цветов.

Методы:
- `get_model()` — возвращает строку: `"Модель: <название модели транспорта>"`.
- `get_horsepower()` — возвращает строку: `"Мощность двигателя: <мощность>"`.
- `get_color()` — возвращает строку: `"Цвет: <цвет транспорта>"`.
- `print_info()` — выводит результаты методов `get_model`, `get_horsepower`, `get_color` и владельца.
- `set_color(new_color)` — меняет цвет, если он есть в `__COLOR_VARIANTS`, иначе выводит сообщение.

#### Класс Sedan (наследник Vehicle):
Атрибут:
- `__PASSENGERS_LIMIT = 5` — лимит пассажиров.

#### Пункты задачи:
1. Создайте классы `Vehicle` и `Sedan`.
2. Определите атрибуты и методы в обоих классах.
3. Убедитесь, что `Sedan` наследуется от `Vehicle`.
4. Создайте объект класса `Sedan` и проверьте работу всех методов.

Пример выполнения программы:
```python
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем изменения
vehicle1.print_info()
```

Ожидаемый вывод:
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos
Невозможно покрасить в Pink
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: BLACK
Владелец: Vasyok

Примечания:
- Константные значения (`__COLOR_VARIANTS`, `__PASSENGERS_LIMIT`) пишите капсом.
- Методы для доступа к атрибутам начинайте с `get` и `set`.
- Используйте `self` для обращения к атрибутам объекта.
'''