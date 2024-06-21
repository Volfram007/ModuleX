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
