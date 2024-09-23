from fastapi import FastAPI
from Module17.task5.routers import task, user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager. [ 127.0.0.1:8000/docs ]"}


app.include_router(task.router)
app.include_router(user.router)

# создаем миграции
# cmd: alembic init Module17/task4/migrations
# В alembic.ini указываем
# sqlalchemy.url = sqlite:///taskmanager.db
# В файле env.py ищем target_metadata = None и устанавливаем:
# from Module17.task5.backend.db import Base
# from Module17.task5.models.task import Task
# from Module17.task5.models.user import User
# target_metadata = Base.metadata
# cmd: alembic revision --autogenerate -m "initial migration"
# Применяем миграцию
# cmd: alembic upgrade head
