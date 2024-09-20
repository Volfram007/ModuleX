from fastapi import FastAPI
from Module17.task1.routers import task
from Module17.task1.routers import user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager. [127.0.0.1:8000/docs]"}


app.include_router(task.router)
app.include_router(user.router)
