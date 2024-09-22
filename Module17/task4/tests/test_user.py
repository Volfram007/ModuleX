from fastapi.testclient import TestClient
from Module17.task4.main import app
import pytest

# Создаём тестовый клиент
client = TestClient(app)

# Тестовые данные для создания нескольких пользователей
test_create = [
    {
        "username": "user1",
        "firstname": "Pasha",
        "lastname": "Technique",
        "age": 40
    },
    {
        "username": "user2",
        "firstname": "Roza",
        "lastname": "Syabitova",
        "age": 62
    },
    {
        "username": "user3",
        "firstname": "Alex",
        "lastname": "Unknown",
        "age": 25
    }
]


@pytest.mark.parametrize("user_data", test_create)
def test_create_users(user_data):
    # Отправка POST-запроса для создания пользователя
    response = client.post("/user/create", json=user_data)
    # Проверка, что статус код 200
    assert response.status_code == 200
    # Проверка, что транзакция успешна
    assert response.json() == {"status_code": 201, "transaction": "Successful"}


def test_update_user():
    # Обновление пользователя с id=3
    user_data = {
        "firstname": "Bear",
        "lastname": "Grylls",
        "age": 50
    }
    response = client.put("/user/update?id=3", json=user_data)

    # Проверка, что статус код 200
    assert response.status_code == 200
    # Проверка, что транзакция успешна
    assert response.json() == {"status_code": 200, "transaction": "User update is successful!"}


def test_delete_user():
    # Удаление пользователя с id=2
    response = client.delete("/user/delete?id=2")

    # Проверка, что статус код 200
    assert response.status_code == 200
    # Проверка, что транзакция успешна
    assert response.json() == {"status_code": 200, "transaction": "User delete is successful!"}


def test_get_all_users():
    # Получение всех пользователей
    response = client.get("/user/")

    # Проверка, что статус код 200
    assert response.status_code == 200
    # Проверка, что возвращается список пользователей
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0


def test_update_non_existent_user():
    # Попытка обновления несуществующего пользователя
    user_data = {
        "firstname": "Non",
        "lastname": "Existent",
        "age": 30
    }
    response = client.put("/user/update?id=999", json=user_data)  # id=999 не существует

    # Проверка, что статус код 404
    assert response.status_code == 404
    # Проверка текста ошибки
    assert response.json() == {"detail": "User was not found"}


def test_delete_non_existent_user():
    # Попытка удаления несуществующего пользователя
    response = client.delete("/user/delete?id=999")  # id=999 не существует

    # Проверка, что статус код 404
    assert response.status_code == 404
    # Проверка текста ошибки
    assert response.json() == {"detail": "User was not found"}

# Запуск по: pytest Module17/task4/tests/test_user.py
