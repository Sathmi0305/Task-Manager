from sqlalchemy import String, Enum as SAEnum, func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime
from app.models.task import TaskStatus
 
class Base(DeclarativeBase):
    pass
 
class Task(Base):
    __tablename__ = 'tasks'
 
    id:         Mapped[int]        = mapped_column(primary_key=True)
    title:      Mapped[str]        = mapped_column(String(255))
    status:     Mapped[TaskStatus] = mapped_column(SAEnum(TaskStatus))
    created_at: Mapped[datetime]   = mapped_column(server_default=func.now())
