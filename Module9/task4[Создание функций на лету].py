from random import choice


class MysticBall:
    def __init__(self, *list_words):
        self.list_words = list_words

    def __call__(self):
        return choice(self.list_words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
'''** Метод __call__ **'''

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda f, s: f == s, first, second))
print(result)
'''** Lambda-функция **'''


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for item in data_set:
                f.write(str(item))
                f.write('\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
'''** Замыкание **'''

'''
### Задача "Функциональное разнообразие"
1. **Lambda-функция:**
   - Даны две строки: `first = 'Мама мыла раму'` и `second = 'Рамена мало было'`.
   - Составьте lambda-функцию для выражения `list(map(?, first, second))`.
   - Результат должен быть списком совпадения букв в той же позиции:
   `[False, True, True, False, False, False, False, False, True, False, False, False, False, False]`.
2. **Замыкание:**
   - Напишите функцию `get_advanced_writer(file_name)`, принимающую название файла для записи.
   - Внутри этой функции определите `write_everything(*data_set)`, которая добавляет в файл `file_name`
   все данные из `data_set` в том же виде.
   - `get_advanced_writer` должна возвращать функцию `write_everything`.
3. **Метод __call__:**
   - Создайте класс `MysticBall` с атрибутом `words`, хранящим коллекцию строк.
   - Определите метод `__call__`, который случайным образом выбирает и возвращает слово из `words` с помощью `random.choice`.

Пример использования кода:
```python
# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(result)  # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# Замыкание:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__
from random import choice

...

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Да, Нет, или Наверное (случайный выбор)
print(first_ball())  # Да, Нет, или Наверное (случайный выбор)
print(first_ball())  # Да, Нет, или Наверное (случайный выбор)
```

### Примечания:
- Все задания пишутся в одном модуле.
- Передаваемые данные в функции и объекты можете использовать свои, главное, чтобы код демонстрировал требуемую логику.
'''
