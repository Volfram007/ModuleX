import sqlite3

# Путь к файлу базы данных
db_path = 'not_telegram.db'


def create_database(path):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    connect.execute('DROP TABLE IF EXISTS Users')

    cursor.execute('''
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY,
            UserName TEXT NOT NULL,
            Email TEXT NOT NULL,
            Age INTEGER,
            Balance INTEGER NOT NULL
        );
    ''')

    # Заполняем таблицу
    [cursor.execute('INSERT INTO Users (UserName, Email, Age, Balance) VALUES (?,?,?,?)',
                    (f'User{i}', f'example{i}@gmail.com', f'{i}0', f'1000')) for i in range(1, 11)]

    # Обновляем каждую вторую запись
    cursor.execute('UPDATE Users SET balance=? WHERE id % 2 = 1', ('500',))

    # Удаляем каждую третью запись
    cursor.execute('DELETE FROM users WHERE id % 3 = 1')

    # Выполнение запроса с условием age != 60
    cursor.execute('SELECT username, email, age, balance FROM users WHERE age != 60')

    # Отправляем изменения в базу данных
    connect.commit()

    # Получение всех результатов
    users = cursor.fetchall()

    # Вывод результатов
    for user in users:
        username, email, age, balance = user
        print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

    # Закрываем соединение
    connect.close()


create_database(db_path)

# **Задача "Первые пользователи"**#
# 1. Создайте файл базы данных `not_telegram.db` и подключитесь к ней, используя библиотеку `sqlite3`.#
# 2. Создайте объект курсора и выполните следующие действия с помощью SQL-запросов:#
# 3. Создайте таблицу `Users`, если она ещё не создана, с полями:
#    - `id` - целое число, первичный ключ
#    - `username` - текст (не пустой)
#    - `email` - текст (не пустой)
#    - `age` - целое число
#    - `balance` - целое число (не пустой)
# 4. Заполните таблицу 10 записями:
#    - User1, example1@gmail.com, 10, 1000
#    - User2, example2@gmail.com, 20, 1000
#    - User3, example3@gmail.com, 30, 1000
#    - ...
#    - User10, example10@gmail.com, 100, 1000
# 5. Обновите `balance` у каждой 2-й записи, начиная с 1-й, на 500:
#    - User1, example1@gmail.com, 10, 500
#    - User2, example2@gmail.com, 20, 1000
#    - User3, example3@gmail.com, 30, 500
#    - ...
#    - User10, example10@gmail.com, 100, 1000
# 6. Удалите каждую 3-ю запись в таблице, начиная с 1-й:
#    - User2, example2@gmail.com, 20, 1000
#    - User3, example3@gmail.com, 30, 500
#    - User5, example5@gmail.com, 50, 500
#    - ...
#    - User9, example9@gmail.com, 90, 500
# 7. Сделайте выборку всех записей, где возраст не равен 60, с помощью `fetchall()`, и выведите их в консоль в формате:
#    - Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
#
# **Пример результата:**
# Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
# Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
# Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
# Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
# Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500
