from Module17.task5.models import User, Task
from Module17.task5.schemas import CreateUser, UpdateUser
from Module17.task5.backend.db_depends import get_db
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])

# Получение всех пользователей
@router.get("/")
def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

# Получение пользователя по id
@router.get("/user_id")
def get_user(db: Annotated[Session, Depends(get_db)], id: int):
    user = db.scalars(select(User).where(User.id == id))
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

# Создание пользователя
@router.post("/create")
def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    # Проверка на существование пользователя
    existing_user = db.scalars(select(User).where(User.username == create_user.username)).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this username already exists")

    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

# Обновление переменных пользователя по id
@router.put("/update")
def update_user(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, id: int):
    user = db.scalars(select(User).where(User.id == id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User was not found')

    db.execute(update(User).where(User.id == id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}

# Удаление пользователя по id
@router.delete("/delete")
def delete_user(db: Annotated[Session, Depends(get_db)], id: int):
    # Проверка на существование пользователя
    user = db.scalars(select(User).where(User.id == id)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    # Удаление всех задач, связанных с пользователем
    db.execute(delete(Task).where(Task.user_id == id))

    db.execute(delete(User).where(User.id == id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}

# Удаление всех пользователей из базы данных
@router.delete("/deleteAllUsers")
def delete_all_users(db: Annotated[Session, Depends(get_db)]):
    # Проверяем, есть ли пользователи в базе данных
    result = db.execute(select(User)).scalars().all()

    if result:  # Если список пользователей не пуст
        db.execute(delete(User))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'All users deleted!'}
    else:  # Если список пользователей пуст
        return {'status_code': status.HTTP_200_OK, 'transaction': 'No users to delete'}

# Получение всех задач пользователя по id
@router.get("/user_id/tasks")
def tasks_user_id(db: Annotated[Session, Depends(get_db)], id: int):
    tasks = db.scalars(select(Task).where(Task.user_id == id)).all()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No tasks found for this user")
    return tasks
