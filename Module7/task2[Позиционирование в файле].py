def custom_write(file_name, strings):
    res = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, s in enumerate(strings):
            res[str(i+1), file.tell()] = s
            file.write(s + '\n')
    return res


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

'''
### Задача "Записать и запомнить"
Создайте функцию `custom_write(file_name, strings)`, которая принимает:
- `file_name` — название файла для записи.
- `strings` — список строк для записи.

Функция должна:
1. Записывать в файл `file_name` все строки из списка `strings`, каждая на новой строке.
2. Возвращать словарь `strings_positions`, где ключ — кортеж `(номер строки, байт начала строки)`, а значение — записываемая строка. Для получения номера байта начала строки используйте метод `tell()` перед записью.

Пример полученного словаря:
```python
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
```
- 1, 2 — номера записанных строк.
- 0, 16 — номера байт, на которых началась запись строк.
- 'Text for tell.', 'Используйте кодировку utf-8.' — сами строки.

#### Пример выполнения программы:
```python
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
```

#### Примечания:
- При записи в файл добавляйте спец. символ перехода на новую строку ('\n').
- Закрывайте файл, вызывая метод `close()` у объектов файла.
- Для работы с символами вне таблицы ASCII используйте кодировку `utf-8`.
'''
