from fastapi import APIRouter, Depends, status, HTTPException
from app.models import *
from sqlalchemy.orm import Session

from typing import Annotated
from app.schemas import CreateUser, UpdateUser, CreateTask, UpdateTask
from slugify import slugify


from app.models.user import User
from app.models.task import Task
from app.backend.db_depends import get_db
from sqlalchemy import select, update, insert
router = APIRouter(prefix="/task", tags=["task"])


# get '/' с функцией all_tasks.
# get '/task_id' с функцией task_by_id.
# post '/create' с функцией create_task.
# put '/update' с функцией update_task.
# delete '/delete' с функцией delete_task.
db_connect = Annotated[Session, Depends(get_db)]
@router.get("/")
async def all_tasks(db: db_connect):
    task_all = db.scalars(select(Task)).all()
    if not task_all:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no tasks'
        )
    return task_all



@router.get("/{task_id}")
async def task_by_id(db: db_connect, task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is not None:
        return task
    else:
        raise HTTPException(status_code=404, detail="Task was not found")


@router.post("/create")
async def create_task(db: db_connect, created_task: CreateTask, user_id : int):
    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(insert(Task).values(
        title=created_task.title,
        content=created_task.content,
        priority=created_task.priority,
        user_id=created_task.user_id,
        slug=slugify(created_task.title)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put("/update")
async def update_task(db : db_connect, task_id: int, update_task: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))

    if task is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User is not found'
        )
    db.execute(update(Task).where(Task.id == task_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'User update is successful'
    }

@router.delete("/delete")
async def delete_task(db: db_connect, task_id: int):
    task = db.query(User).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='task is not found'
        )
    db.delete(task)
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'task delete is successful'
    }


# Создайте новый маршрут get "/user_id/tasks" и функцию tasks_by_user_id.
# Логика этой функции должна заключатся в возврате всех Task конкретного User по id.
# Дополните функцию delete_user так, чтобы вместе с пользователем удалялись
# все записи связанные с ним.

@router.delete("/{user_id}/tasks")
async def tasks_by_user_id(db: db_connect, user_id: int):
    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return tasks
