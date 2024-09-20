from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return 'Главная страница'


@app.get("/user/{user_id}")
async def user(user_id: int = Path(ge=1, le=100, description='Enter Id', example=12)):
    return f'Пользователь {user_id}'


@app.get("/user/{name}/{age}")
async def user(name: Annotated[str, Path(min_length=5, max_length=20, description='Enter Name', example='Иванов')],
               age: Annotated[int, Path(ge=18, le=120, description='Enter Age', example=18)]):
    return f'Пользователь {name} {age}'

# Основные ограничения и типы:
# gt: Greater than (больше)
# ge: Greater than or equal to (больше или равно)
# lt: Less than (меньше)
# le: Less than or equal to (меньше или равно)
# ...: Обязательный параметр
# None: Необязательный параметр
