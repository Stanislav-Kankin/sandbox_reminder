from sqlalchemy import (create_engine, Column, Integer,
                        String, Boolean, DateTime)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class ReminderBase(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(DateTime, nullable=False)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"Reminder(id={self.id}, title='{self.title}', due_date='{self.due_date}')"


# Создание движка SQLite
engine = create_engine('sqlite:///reminders.db')

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Создание таблицы
Base.metadata.create_all(engine)
