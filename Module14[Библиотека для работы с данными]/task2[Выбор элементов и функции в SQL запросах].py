import sqlite3

# Путь к файлу базы данных
db_path = 'not_telegram.db'


def create_database(path):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    """
        Раскомментировать для создания таблицы
    """
    # connect.execute('DROP TABLE IF EXISTS Users')
    # cursor.execute('''
    #     CREATE TABLE Users (
    #         id INTEGER PRIMARY KEY,
    #         UserName TEXT NOT NULL,
    #         Email TEXT NOT NULL,
    #         Age INTEGER,
    #         Balance INTEGER NOT NULL
    #     );
    # ''')
    # # Заполняем таблицу
    # [cursor.execute('INSERT INTO Users (UserName, Email, Age, Balance) VALUES (?,?,?,?)',
    #                 (f'User{i}', f'Example{i}@gmail.com', f'{i}0', f'1000')) for i in range(1, 11)]
    # # Обновляем каждую вторую запись
    # cursor.execute('UPDATE Users SET balance=? WHERE id % 2 = 1', ('500',))
    # # Удаляем каждую третью запись
    # cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
    # # Отправляем изменения в базу данных
    # connect.commit()

    # Удаляем пользователя с id = 6
    cursor.execute('DELETE FROM Users WHERE id = 6')
    # Получение среднего баланса
    cursor.execute('SELECT AVG(Balance) FROM Users')
    balances = cursor.fetchone()[0]
    print(f"Среднее: {balances}")

    # cursor.execute('SELECT Balance FROM Users')
    # balances = cursor.fetchall()
    # print(f"Среднее: {sum(balance[0] for balance in balances)/len(balances)}")

    # Закрываем соединение
    connect.close()


create_database(db_path)

# **Задача "Средний баланс пользователя"**
# 1. Удалите запись с `id = 6` из базы данных `not_telegram.db`.
# 2. Подсчитайте общее количество записей.
# 3. Подсчитайте сумму всех балансов.
# 4. Выведите в консоль средний баланс всех пользователей.
#
# **Пример результата:**
# 700.0
