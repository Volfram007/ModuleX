from fastapi import FastAPI, Path, HTTPException
from typing import List
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()

db = []


class User(BaseModel):
    id: int = None
    name: str
    age: int


@app.get("/")
async def root() -> str:
    return '127.0.0.1:8000/docs'


@app.get("/user")
async def get_all_db() -> List[User]:
    return db


@app.post('/user/{username}/{age}')
async def add_user(username: str = Path(example='User'),
                   age: int = Path(example=28)) -> str:
    id_new = len(db)
    db.append(User(id=id_new, name=username, age=age))
    return f"User {int(id_new) + 1} is registered"


@app.put('/user/{id}/{username}/{age}')
async def update_user(id: int = Path(example=1), username: str = Path(example='new User'),
                      age: int = Path(example=18)) -> str:
    try:
        db[id].name = username
        db[id].age = age
        return f"User {id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete('/user/{id}')
async def delete_user(id: int = Path(example=1)) -> str:
    try:
        del db[id]
        return f"User {id} is deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


client = TestClient(app)


# создание тестов
def test_get(test: str):
    response = client.get(test)
    print(f'{response} - {test}')


def test_post(test: str):
    response = client.post(test)
    print(f'{response} - {test}')


def test_put(test: str):
    response = client.put(test)
    print(f'{response} - {test}')


def test_delete(test: str):
    response = client.delete(test)
    print(f'{response} - {test}')


test_get("/user")
test_post("/user/UrbanUser/24")
test_post("/user/UrbanTest/36")
test_post("/user/Admin/42")
test_put("/user/1/UrbanProfi/28")
test_delete("/user/2")
test_delete("/user/2")
