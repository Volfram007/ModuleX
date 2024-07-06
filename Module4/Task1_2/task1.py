from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Тестирование функций
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)  # 23.0
print(result2)  # Ошибка
print(result3)  # 7.0
print(result4)  # inf

'''
**Задача "А как делить?"**
Создайте два модуля `fake_math` и `true_math`, в каждом из которых будет функция `divide` для деления с разными подходами.

1. **Модуль `fake_math`**:
   - Функция `divide(first, second)` возвращает результат деления `first` на `second`.
   - Если `second` равно 0, функция возвращает строку `'Ошибка'`.

2. **Модуль `true_math`**:
   - Функция `divide(first, second)` возвращает результат деления `first` на `second`.
   - Если `second` равно 0, функция возвращает бесконечность (`math.inf`).

**Пункты задачи:**
1. Создайте модули `fake_math` и `true_math`.
2. Напишите функцию `divide` в каждом модуле с соответствующей логикой.
3. Создайте модуль `module_4_1`.
4. Импортируйте функции `divide` из модулей `fake_math` и `true_math` в `module_4_1`, используя оператор `as` для избежания конфликта имён.
5. Вызовите эти функции в `module_4_1`, передав первым аргументом произвольное число, отличное от 0, а вторым аргументом - 0.
6. Выведите результаты вызовов этих функций на экран.

**Пример выполнения программы:**
```python
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)  # 23.0
print(result2)  # Ошибка
print(result3)  # 7.0
print(result4)  # inf
```

**Примечания:**
- Импортируйте бесконечность из библиотеки `math` (`from math import inf`).
- Деление выполняйте с использованием оператора `/`.
- При импорте функций `divide` из разных модулей используйте переопределение имён.
'''