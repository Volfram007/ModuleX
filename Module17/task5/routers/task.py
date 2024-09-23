from Module17.task5.models import Task, User
from Module17.task5.schemas import CreateTask, UpdateTask
from Module17.task5.backend.db_depends import get_db
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])

# Получение всех задач
@router.get("/")
def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

# Получение задачи по id
@router.get("/task_id")
def get_task(db: Annotated[Session, Depends(get_db)], id: int):
    task = db.scalars(select(Task).where(Task.id == id)).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    return task

# Создание задачи
@router.post("/create")
def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, id: int):
    # Проверка, существует ли пользователь
    user = db.scalars(select(User).where(User.id == id)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    db.execute(insert(Task).values(
        title=create_task.title,
        content=create_task.content,
        priority=create_task.priority,
        user_id=create_task.user_id,
        slug=slugify(create_task.title), ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

# Обновление задачи по id
@router.put("/update")
def update_task(db: Annotated[Session, Depends(get_db)], update_task: UpdateTask, id: int):
    task = db.scalars(select(Task).where(Task.id == id)).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')

    db.execute(update(Task).where(Task.id == id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

# Удаление задачи по id
@router.delete("/delete")
def delete_task(db: Annotated[Session, Depends(get_db)], id: int):
    task = db.scalars(select(Task).where(Task.id == id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')

    db.execute(delete(Task).where(Task.id == id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}

# Удаление всех задач
@router.delete("/deleteAllTask")
def delete_all_users(db: Annotated[Session, Depends(get_db)]):
    # Проверяем, есть ли задания в базе данных
    result = db.execute(select(Task)).scalars().all()

    if result:  # Если список пользователей не пуст
        db.execute(delete(Task))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'All task deleted!'}
    else:  # Если список пользователей пуст
        return {'status_code': status.HTTP_200_OK, 'transaction': 'No task to delete'}
