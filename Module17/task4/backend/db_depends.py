from Module17.task4.backend.db import Session


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
