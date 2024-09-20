from fastapi import FastAPI, Path, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.testclient import TestClient

app = FastAPI()
templates = Jinja2Templates(directory="Module16/templates")


class User(BaseModel):
    id: int = None
    username: str
    age: int


users_db = []


@app.get("/")
async def root(request: Request) -> HTMLResponse:
    # return '127.0.0.1:8000/docs'
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})


@app.post('/user/{username}/{age}')
async def add_user(username: str = Path(example='User'),
                   age: int = Path(example=28)) -> str:
    id_new = len(users_db)
    users_db.append(User(id=id_new, username=username, age=age))
    return f"User {int(id_new) + 1} is registered"


@app.get("/users/{user_id}")
async def get_user(request: Request, user_id: int):
    if 0 <= user_id < len(users_db):
        user = users_db[user_id]
        return templates.TemplateResponse("users.html", {"request": request, "user": user})
    else:
        return {"error: User not found"}


client = TestClient(app)


# создание тестов
def test_post(test: str):
    response = client.post(test)
    print(f'{response} - {test}')


test_post("/user/UrbanUser/24")
test_post("/user/UrbanTest/36")
test_post("/user/Capybara/60")
test_post("/user/Admin/11")
