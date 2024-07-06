class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()  # Чтение всего содержимого файла и удаление лишних пробелов
        except FileNotFoundError:
            return ''

    def add(self, *products):
        current_products = self.get_products().splitlines()  # Загружаем список продуктов из файла
        current_product_names = {line.split(', ')[0] for line in current_products}  # Извлечение имен продуктов
        # print('--', current_product_names)
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:  # Проход по всем переданным продуктам
                if product.name not in current_product_names:  # Проверка, если продукт еще не добавлен
                    file.write(str(product) + '\n')  # Запись продукта в файл
                    current_product_names.add(product.name)  # Добавление имени продукта в список
                else:
                    print(f'\033[35mПродукт {product.name} уже есть в магазине\033[0m')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)
print(s1.get_products())

'''
### Задача "Учёт товаров"
Реализуйте два класса `Product` и `Shop` для записи продуктов в файл.

#### Класс Product:
Атрибуты:
- `name` — название продукта (строка).
- `weight` — вес товара (дробное число).
- `category` — категория товара (строка).

Методы:
- `__str__` — возвращает строку в формате '<название>, <вес>, <категория>'.

#### Класс Shop:
Атрибуты:
- `__file_name = 'products.txt'` (инкапсулированный).

Методы:
- `get_products(self)` — считывает и возвращает всю информацию из файла `__file_name`.
- `add(self, *products)` — принимает неограниченное количество объектов класса `Product`. 
Добавляет каждый продукт в файл `__file_name`, если его ещё нет в файле (по названию). 
Если продукт уже существует, выводит сообщение 'Продукт <название> уже есть в магазине'.

#### Пример выполнения программы:
```python
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())
```

#### Примечания:
- При записи в файл добавляйте символ перехода на новую строку ('\n').
- Для проверки наличия товара в методе `add` используйте метод `get_products`.
- Не забывайте закрывать файл, вызывая метод `close()` у объектов файла.
'''
