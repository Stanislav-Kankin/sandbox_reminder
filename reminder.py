from datetime import datetime
from typing import List, Optional
from database import session, ReminderBase


class Reminder:
    def __init__(self, title: str,
                 description: Optional[str] = None,
                 due_date: Optional[datetime] = None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def save(self):
        reminder = ReminderBase(
            title=self.title,
            description=self.description,
            due_date=self.due_date,
            completed=self.completed
        )
        session.add(reminder)
        session.commit()

    @staticmethod
    def get_all() -> List[ReminderBase]:
        return session.query(ReminderBase).all()

    @staticmethod
    def get_by_id(reminder_id: int) -> Optional[ReminderBase]:
        return session.query(ReminderBase).filter_by(id=reminder_id).first()

    @staticmethod
    def update(reminder_id: int, **kwargs):
        reminder = session.query(ReminderBase).filter_by(id=reminder_id).first()
        if reminder:
            for key, value in kwargs.items():
                setattr(reminder, key, value)
            session.commit()

    @staticmethod
    def delete(reminder_id: int):
        reminder = session.query(ReminderBase).filter_by(id=reminder_id).first()
        if reminder:
            session.delete(reminder)
            session.commit()
