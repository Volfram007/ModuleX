# Запуск по: pytest Module17/task5/tests/test_user.py
from fastapi.testclient import TestClient
from Module17.task5.main import app
import pytest

# Создаём тестовый клиент
client = TestClient(app)


# Удаляем всех пользователей
def test_delete_all_users():
    response = client.delete("/user/deleteAllUsers")

    assert response.status_code == 200
    if response.json() == {"transaction": "All users deleted"}:
        assert response.json() == {"transaction": "All users deleted"}
    elif response.json() == {"transaction": "No users to delete"}:
        assert response.json() == {"transaction": "No users to delete"}


# Тестовые данные для создания нескольких пользователей
list_user = [
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


# Тестовые данные для создания пользователя
@pytest.mark.parametrize("user_data", list_user)
def test_create_users(user_data):
    # Отправка POST-запроса для создания пользователя
    response = client.post("/user/create", json=user_data)
    # Проверка, что статус код 200
    assert response.status_code == 200
    # Проверка, что транзакция успешна
    assert response.json() == {"status_code": 201, "transaction": "Successful"}


def test_get_users():
    # Отправка GET-запроса для создания пользователя
    response = client.get("/user/user_id?id=3")
    # Проверка, что статус код 200
    assert response.status_code == 200
    # Проверка, что транзакция успешна
    data = response.json()
    # Проверка структуры ответа
    assert data["status_code"] == 200
    assert data["transaction"] == "Successful"
    assert data["user"]["id"] == 3


# Тестовые данные для обновления пользователя
def test_update_user():
    # Обновление пользователя с id=3
    user_data = {
        "firstname": "Bear",
        "lastname": "Grylls",
        "age": 50
    }
    response = client.put("/user/update", params={"id": 3}, json=user_data)

    # Проверка, что статус код 200
    assert response.status_code == 200
    # Проверка, что транзакция успешна
    assert response.json() == {"status_code": 200, "transaction": "User update is successful!"}


# Тестовые данные для удаления пользователя
def test_delete_user():
    # Удаление пользователя с id=2
    response = client.delete("/user/delete", params={"id": 2})

    # Проверка, что статус код 200
    assert response.status_code == 200
    # Проверка, что транзакция успешна
    assert response.json() == {"status_code": 200, "transaction": "User delete is successful!"}


# Тестовые данные для получения всех пользователей
def test_get_all_users():
    response = client.get("/user/")

    assert response.status_code == 200
    # Проверка, что возвращается список пользователей
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0


# Попытка обновления несуществующего пользователя
def test_update_non_existent_user():
    user_data = {
        "firstname": "Non",
        "lastname": "Existent",
        "age": 30
    }
    response = client.put("/user/update", params={"id": 999}, json=user_data)  # id=999 не существует

    # Проверка, что статус код 404
    assert response.status_code == 404
    # Проверка текста ошибки
    assert response.json() == {"detail": "User was not found"}


# Попытка удаления несуществующего пользователя
def test_delete_non_existent_user():
    response = client.delete("/user/delete", params={"id": 999})  # id=999 не существует

    # Проверка, что статус код 404
    assert response.status_code == 404
    # Проверка текста ошибки
    assert response.json() == {"detail": "User was not found"}


# Удаляем все задания
def test_delete_all_task():
    response = client.delete("/task/deleteAllTask")

    assert response.status_code == 200
    if response.json() == {"transaction": "All task deleted"}:
        assert response.json() == {"transaction": "All task deleted"}
    elif response.json() == {"transaction": "No task to delete"}:
        assert response.json() == {"transaction": "No task to delete"}


list_tasks = [
    {"title": "FirstTask", "content": "Content1", "priority": 0, "user_id": 1},
    {"title": "SecondTask", "content": "Content2", "priority": 2, "user_id": 1},
    {"title": "ThirdTask", "content": "Content3", "priority": 4, "user_id": 3},
    {"title": "FourthTask", "content": "Content4", "priority": 6, "user_id": 3}
]


# Тестовые данные для создания нескольких задач
@pytest.mark.parametrize("task_data", list_tasks)
def test_create_tasks_for_users(task_data):
    response = client.post(f"/task/create", params={"id": task_data['user_id']}, json=task_data)
    assert response.json() == {"status_code": 201, "transaction": "Successful"}


# Удаление задачи
def test_delete_task():
    response = client.delete("/task/delete", params={"id": 3})
    assert response.status_code == 200


# Тестовое удаление пользователя и его задач
def test_delete_user_with_tasks():
    response = client.delete("/user/delete", params={"id": 1})
    assert response.status_code == 200

    # Проверка, что задачи пользователя также были удалены
    response_tasks = client.get("/task/")
    tasks = response_tasks.json()
    assert all(task["user_id"] != 1 for task in tasks)

# Обновление переменных задач
# def test_update_task():
#     task_data = {
#         "title": "Task1",
#         "content": "UpdateTask",
#         "priority": 50
#     }
#     response = client.put("/task/update", params={"id": 4}, json=task_data)
#
#     assert response.status_code == 200
#     assert response.json() == {"status_code": 200, "transaction": "Task update is successful!"}


