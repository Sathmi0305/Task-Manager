from fastapi import APIRouter
from app.models.task import TaskCreate, TaskRead
from datetime import datetime
 
router = APIRouter(prefix='/tasks', tags=['Tasks'])
 
# Temporary in-memory list (we will add a real database in Step 4)
fake_db: list[dict] = []
next_id = 1

@router.get('/', response_model=list[TaskRead])
async def list_tasks():
    return fake_db
 
@router.post('/', response_model=TaskRead, status_code=201)
async def create_task(payload: TaskCreate):
    global next_id
    task = {
        'id':         next_id,
        'title':      payload.title,
        'status':     payload.status,
        'created_at': datetime.now()
    }
    fake_db.append(task)
    next_id += 1
    return task

