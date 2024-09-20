from fastapi import FastAPI
from routers import task
from routers import user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager. [127.0.0.1:8000/docs]"}


app.include_router(task.router)
app.include_router(user.router)
