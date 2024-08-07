import sqlite3 as sql
import logging as log
import os

# Путь к файлу базы данных
db_path = 'Config/database.db'

base = \
    ("""
AMD Ryzen 9 7950X | 16 ядер, 32 потока, 5.7 ГГц | 120000 | https://main-cdn.sbermegamarket.ru/big2/hlr-system/170/212/126/212/710/45/100065398356b0.jpg
Intel Core i9-13900K | 24 ядра, 32 потока, 5.8 ГГц | 130000 | https://main-cdn.sbermegamarket.ru/big2/hlr-system/153/118/019/433/023/47/100050679145b0.jpg
AMD Ryzen 9 7900X | 12 ядер, 24 потока, 5.6 ГГц | 90000 | https://main-cdn.sbermegamarket.ru/big2/hlr-system/170/212/126/212/710/45/100065398356b0.jpg
Intel Core i7-13700K | 16 ядер, 24 потока, 5.4 ГГц | 80000 | https://main-cdn.sbermegamarket.ru/big2/hlr-system/153/118/019/433/023/47/100050679145b0.jpg
AMD Ryzen 7 7800X | 8 ядер, 16 потоков, 5.3 ГГц | 60000 | https://main-cdn.sbermegamarket.ru/big2/hlr-system/170/212/126/212/710/45/100065398356b0.jpg
Intel Core i5-13600K | 14 ядер, 20 потоков, 5.1 ГГц | 50000 | https://main-cdn.sbermegamarket.ru/big2/hlr-system/153/118/019/433/023/47/100050679145b0.jpg
""")


def initiate_db() -> None:
    if os.path.exists(db_path):
        log.info('Файл БД существует')
        return
    else:
        log.info('Создание базы данных')

    conn = sql.connect(db_path)
    cursor = conn.cursor()
    # Создаем таблицу с товарами
    cursor.execute('DROP TABLE IF EXISTS Products')
    cursor.execute('''
            CREATE TABLE Products (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL,
                link TEXT NOT NULL
            )''')

    # Создаем таблицу с пользователями
    cursor.execute('DROP TABLE IF EXISTS Users')
    cursor.execute('''
            CREATE TABLE Users (
                id INTEGER PRIMARY KEY,
                id_user INTEGER NOT NULL,
                login TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
            )''')

    # Разделяем текст на строки и обрабатываем каждую строку
    for line in base.split('\n'):
        # Разделяем строку на столбцы
        col = line.split(' | ')
        if len(col) == 4:
            # Извлекаем информацию о продукте
            title, desc, price, link = col
            cursor.execute('''INSERT INTO Products (title, description, price, link)
                VALUES (?, ?, ?, ?)
            ''', (title, desc, price, link))

    conn.commit()
    conn.close()


def get_all_products() -> list:
    conn = sql.connect('Config/database.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM Products')
        # Получаем результат запроса
        result = cursor.fetchall()

        return result
    except sql.Error as e:
        log.critical(f"sqlError: {e}")
        return []
    except Exception as e:
        log.critical(f"Ошибка: {e}")
        return []
    finally:
        conn.close()


def is_validlogin(login) -> bool:
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM Users WHERE login=?", (login,))
        users = cursor.fetchone()[0]
        if users > 0:
            return True  # Если пользователь существует
        else:
            return False  # Если пользователь не существует
    except sql.Error as e:
        log.critical(f"sqlError: {e}")
        return False
    except Exception as e:
        log.critical(f"Ошибка: {e}")
        return False
    finally:
        conn.close()


def is_validemail(email) -> bool:
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM Users WHERE mail=?", (email,))
        users = cursor.fetchone()[0]
        if users > 0:
            return True  # Если почта существует
        else:
            return False  # Если почта не существует
    except sql.Error as e:
        log.critical(f"sqlError: {e}")
        return False
    except Exception as e:
        log.critical(f"Ошибка: {e}")
        return False
    finally:
        conn.close()


def add_user(user_id, login, email, age) -> bool:
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO Users (id_user, login, email, age, balance)
         VALUES (?, ?, ?, ?, ?)
         ''', (user_id, login, email, age, 150_000))
        conn.commit()
    except sql.Error as e:
        log.critical(f"sqlError: {e}")
        return False
    except Exception as e:
        log.critical(f"Ошибка: {e}")
        return False
    finally:
        conn.close()  # Закрываем соединение с базой данных в любом случае
    return True


def buy_product(user_id, product_id):
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM Users WHERE id_user =?', (user_id,))
        client = cursor.fetchone()[5]
        cursor.execute('SELECT * FROM Products WHERE title =?', (product_id,))
        warehouse = int(cursor.fetchone()[3])
        if client >= warehouse:
            cursor.execute('UPDATE Users SET balance = balance -? WHERE id_user =?', (warehouse, user_id))
            conn.commit()
            return True
        else:
            return False
    except sql.Error as e:
        log.critical(f"sqlError: {e}")
        return False
    except Exception as e:
        log.critical(f"Ошибка: {e}")
        return False
    finally:
        conn.close()


def del_user(user_id) -> None:
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(' DELETE FROM Users WHERE id_user =? ', (user_id,))
        conn.commit()
    except sql.Error as e:
        log.critical(f"sqlError: {e}")
    except Exception as e:
        log.critical(f"Ошибка: {e}")
    conn.close()


def info_user(command, user_id) -> list:
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    try:
        if command == 'баланс':
            cursor.execute('SELECT balance FROM Users WHERE id_user =?', (user_id,))
        result = cursor.fetchone()[0]
    except sql.Error as e:
        log.critical(f"sqlError: {e}")
        result = 0
    except Exception as e:
        log.critical(f"Ошибка: {e}")
        result = 0
    finally:
        conn.close()
    return result


def is_included(user_id) -> bool:  # Проверка наличия пользователя в базе
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_user FROM Users WHERE id_user =?", (user_id,))
        result = cursor.fetchone()
        if result is not None:
            result = True
        else:
            result = False  # Если пользователь не найден, то возвращаем False
    except sql.Error as e:
        log.critical(f"sqlError: {e}")
        result = False
    except Exception as e:
        log.critical(f"Ошибка: {e}")
        result = False
    finally:
        conn.close()
    return result
