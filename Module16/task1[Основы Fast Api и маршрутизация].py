from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return 'Главная страница'


@app.get("/user/admin")
async def admin():
    return 'Вы вошли как администратор'


@app.get("/user/{user_id}")
async def user(user_id: int):
    return f'Вы вошли как пользователь {user_id}'


@app.get("/user/{user_id}/{user_age}")
async def user(user_id: int, user_age: int):
    return f'Вы вошли как пользователь {user_id}, возраст {user_age}'
