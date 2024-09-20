from fastapi import FastAPI, Path

app = FastAPI()

users = {"0": "Петя, возраст 18", "1": "Иван, возраст 19"}


@app.get("/")
async def root() -> str:
    return '127.0.0.1:8000/docs'


@app.get("/user")
async def get_all_db() -> dict:
    return users


@app.post('/users/{username}/{age}')
async def add_user(username: str = Path(example='new User'),
                   age: int = Path(example=28)) -> str:
    new_id = str(int(max(users, key=int)) + 1)
    users[new_id] = f'{username}, возраст {age}'
    return f"User {int(new_id) + 1} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str = Path(example='0'),
                      username: str = Path(example='new Name'),
                      age: int = Path(example=81)) -> str:
    users[user_id] = f'{username}, возраст {age}'
    return f"User {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: str = Path(example='0')) -> str:
    users.pop(user_id)
    return f"User {user_id} is deleted"
