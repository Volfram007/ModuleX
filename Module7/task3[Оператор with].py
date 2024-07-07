import os
from string import punctuation

# Директория хранения файлов тестов
directory = 'Test_task3'
test_files_list = {}  # Список файлов для тестов


class WordsFinder:
    def __init__(self, list_file):
        self.list_file = list_file
        self.list_words = {}  # Список слов

    # @staticmethod
    def get_all_words(self):
        for f_name in self.list_file:  # Получаем список файлов для тестов
            with open(self.list_file[f_name], 'r', encoding='utf-8') as file:  # Открываем файл для чтения
                translator = str.maketrans('', '', punctuation)  # Создаем транслятор для удаления пунктуации
                self.list_words[f_name] = file.read().translate(
                    translator).lower().split()  # Получаем без пунктуации в нижнем регистре список слов
        return self.list_words

    def find(self, word_f):
        # Поиск слова из списка и выводим его позицию
        for f_name in self.list_words:
            if word_f in self.list_words[f_name]:
                file_f = os.path.splitext(f_name)[0]  # Получаем имя файла
                return file_f, self.list_words[f_name].index(word_f) + 1

    def count(self, word_c):
        # Подсчет количества вхождений слова в файле
        for f_name in self.list_words:
            if word_c in self.list_words[f_name]:
                file_c = os.path.splitext(f_name)[0]  # Получаем имя файла
                return file_c, self.list_words[f_name].count(word_c)

    def info(self, word_i):
        print(f'{self.find(word_i)}\t\033[0;32m{word_i}\033[0m')
        print(f'{self.count(word_i)}\t\033[0;32m{word_i}\033[0m')


# Поиск файлов для тестов
for root, dirs, files in os.walk(directory):
    for f in files:
        filepath = os.path.join(root, f)  # Получаем путь к файлу
        test_files_list[f] = filepath  # Добавляем список файлов для тестов

# Получаем список слов из файла
finder = WordsFinder(test_files_list)
all_words = finder.get_all_words()

for file_name in all_words:  # Проходим по списку
    w = []
    for word in all_words[file_name]:
        w.append(word)
    file = os.path.splitext(file_name)[0]
    print(f'\033[0;33m{file}\033[0m')  # Выводим имя файла
    print(f'\033[0;32m{w}\033[0m')  # Выводим список слов из файла

finder.info('text')
finder.info('captain')
finder.info('the')
finder.info('child')

'''
### Задача "Найдёт везде"
Напишите класс `WordsFinder`. Объекты этого класса создаются следующим образом: 
`WordsFinder('file1.txt', 'file2.txt', ...)`. Класс должен принимать неограниченное количество названий файлов и 
записывать их в атрибут `file_names` в виде списка или кортежа.

### Методы класса:
#### `get_all_words`
- Возвращает словарь следующего вида:
  ```python
  {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], ...}
  ```
  - Где ключи - названия файлов, значения - списки слов из этих файлов.
- Алгоритм:
  - Создайте пустой словарь `all_words`.
  - Переберите названия файлов и откройте каждый из них с помощью оператора `with`.
  - Прочитайте содержимое файла, приведите его к нижнему регистру.
  - Удалите пунктуацию [',', '.', '=', '!', '?', ';', ':', ' - '].
  - Разбейте строку на список слов с помощью `split()`.
  - Запишите полученные данные в словарь `all_words`, где ключ - название файла, значение - список слов.

#### `find(self, word)`
- Принимает слово `word`.
- Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.

#### `count(self, word)`
- Принимает слово `word`.
- Возвращает словарь, где ключ - название файла, значение - количество вхождений слова `word` в списке слов этого файла.

### Пример использования:
```python
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT'))    # Позиция 3-го слова по счёту
print(finder2.count('teXT'))   # 4 вхождения слова 'teXT'
```

### Примечания:
- При обработке файлов используйте `with` для корректного закрытия файла.
- Для удаления пунктуации используйте метод `replace` или регулярные выражения.
- Для удобного перебора ключей и значений словаря используйте метод `items()`.
'''
