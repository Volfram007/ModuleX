def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру для сравнения
    root_word_lower = root_word.lower()
    same_words = []

    for word in other_words:
        # Приводим текущее слово к нижнему регистру для сравнения
        word_lower = word.lower()
        # Проверяем, содержится ли root_word в слове или слово в root_word
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Добавляем слово в список same_words
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)

'''
**Задача "Однокоренные"**
Напишите функцию `single_root_words`, которая принимает обязательный параметр `root_word` и неограниченную 
последовательность в параметр `*other_words`. Функция должна возвращать список `same_words`, 
содержащий слова из `other_words`, которые включают `root_word` или содержатся в `root_word`.

**Пункты задачи:**
1. Объявите функцию `single_root_words` с параметрами `root_word` и `*other_words`.
2. Создайте пустой список `same_words`.
3. Переберите слова из `other_words` с помощью цикла `for`.
4. Добавляйте слова в `same_words`, если они удовлетворяют условию задачи.
5. Верните список `same_words`.

**Пример выполнения программы:**
```python
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
```

**Примечания:**
- Регистр символов не должен влиять на проверку наличия одного слова в другом.
- Полезные методы: `in`, `count()`, `lower()`, `upper()`.
'''