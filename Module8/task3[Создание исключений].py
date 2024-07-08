# Создание пользовательского исключения
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__set_vin(vin)  # Вызов приватного метода
        self.__set_numbers(numbers)  # Вызов приватного метода

    def __set_vin(self, vin):
        if self.__is_valid_vin(vin):
            self.__vin = vin

    @staticmethod
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __set_numbers(self, numbers):
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    @staticmethod
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


# Примеры использования классов
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

'''
### Задача "Некорректность"
Создайте 3 класса (2 из которых будут исключениями):

#### Класс `Car`
- **Атрибут `model`** - название автомобиля (строка).
- **Атрибут `__vin`** - vin номер автомобиля (целое число). Уровень доступа private.
- **Метод `__is_valid_vin(vin_number)`** - проверяет `vin_number` на корректность. Возвращает `True`, если корректный,
иначе выбрасывает исключение. Уровень доступа private.
- **Атрибут `__numbers`** - номера автомобиля (строка).
- **Метод `__is_valid_numbers(numbers)`** - проверяет `numbers` на корректность. Возвращает `True`, если корректный,
иначе выбрасывает исключение. Уровень доступа private.

#### Классы исключений:
- **`IncorrectVinNumber`** - имеет атрибут `message`, который выводится при выбрасывании исключения.
- **`IncorrectCarNumbers`** - имеет атрибут `message`, который выводится при выбрасывании исключения.

#### Работа методов:
- **`__is_valid_vin(vin_number)`**:
  - Выбрасывает исключение `IncorrectVinNumber` с сообщением 'Некорректный тип vin номер', если передано не целое число.
  - Выбрасывает исключение `IncorrectVinNumber` с сообщением 'Неверный диапазон для vin номера', если число не в
  диапазоне от 1000000 до 9999999 включительно.
  - Возвращает `True`, если исключения не были выброшены.

- **`__is_valid_numbers(numbers)`**:
  - Выбрасывает исключение `IncorrectCarNumbers` с сообщением 'Некорректный тип данных для номеров',
  если передана не строка.
  - Выбрасывает исключение `IncorrectCarNumbers` с сообщением 'Неверная длина номера',
  если строка не состоит из 6 символов.
  - Возвращает `True`, если исключения не были выброшены.

#### Пример выполнения программы:
```python
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
```

#### Вывод на консоль:
Model1 успешно создан
Неверный диапазон для vin номера
Неверная длина номера

#### Примечания:
- Методы `__is_valid_vin` и `__is_valid_numbers` должны вызываться при создании объекта
(в `__init__` при объявлении атрибутов `__vin` и `__numbers`).
- Для выбрасывания исключений используйте оператор `raise`.
'''
