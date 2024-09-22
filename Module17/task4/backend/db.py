from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# создаем базу данных
engine = create_engine('sqlite:///taskmanager.db', echo=True)

Session = sessionmaker(bind=engine)  # создаем сессию


class Base(DeclarativeBase):  # создаем базу данных
    pass
