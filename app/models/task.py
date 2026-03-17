from pydantic import BaseModel
from datetime import datetime
from enum import Enum


# The possible states a task can be in
class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


# What data is needed to CREATE a task
class TaskCreate(BaseModel):
    title: str
    status: TaskStatus = TaskStatus.todo


# What data is returned when you READ a task
class TaskRead(BaseModel):
    id: int
    title: str
    status: TaskStatus
    created_at: datetime

    class Config:
        from_attributes = True
