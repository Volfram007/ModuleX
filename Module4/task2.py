def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()

'''
**Задача "Пространство имен"**
1. Создайте новый проект в PyCharm.
2. Запустите проект.

**Задача:**
1. Создайте функцию `test_function`.
2. Внутри `test_function` создайте функцию `inner_function`, которая печатает 
    "Я в области видимости функции test_function".
3. Вызовите `inner_function` внутри `test_function`.
4. Попробуйте вызвать `inner_function` вне `test_function` и посмотрите на результат выполнения программы.

**Пример кода:**
```python
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
inner_function()  # Это вызовет ошибку
```
'''