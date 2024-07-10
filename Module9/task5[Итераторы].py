class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        res = self.pointer  # возвращаем указатель
        self.pointer += self.step  # увеличиваем указатель на шаг
        return res


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

'''
### Задача "Range - это просто"
1. **Создание пользовательского исключения:**
   - Создайте класс исключения `StepValueError`, наследующийся от `ValueError` и оставьте его пустым.
2. **Создание класса `Iterator`:**
   - Атрибуты объекта:
     - `start`: начальное значение (целое число).
     - `stop`: конечное значение (целое число).
     - `step`: шаг итерации (целое число).
     - `pointer`: текущее значение (изначально равно `start`).
   - Методы:
     - `__init__(self, start, stop, step=1)`: принимает начальное значение, конечное значение и шаг итерации.
     Если `step` равен 0, выбрасывает исключение `StepValueError('шаг не может быть равен 0')`.
     - `__iter__(self)`: сбрасывает `pointer` на `start` и возвращает объект итератора.
     - `__next__(self)`: увеличивает `pointer` на `step`. Завершает итерацию, если `pointer` выходит за пределы `stop`.
3. **Пример использования:**
   - Создайте несколько объектов класса `Iterator`.
   - Совершите итерации с ними при помощи цикла `for`.

Пример выполнения кода:
```python
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
```

### Примечания:
- Особое внимание уделите методу `__next__` и условиям завершения итерации.
'''
