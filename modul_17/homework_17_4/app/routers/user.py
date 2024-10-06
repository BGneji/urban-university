
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from typing import Annotated
from app.schemas import CreateUser, UpdateUser
from slugify import slugify
router = APIRouter(prefix="/user", tags=["user"])
from app.models.user import User
from app.models.task import Task
from app.backend.db_depends import get_db

# from fastapi import APIRouter, Depends, status, HTTPException
# # Сессия БД
# from sqlalchemy.orm import Session
# # Функция подключения к БД
# from backend.db_depends import get_db
# # Аннотации, Модели БД и Pydantic.
# from typing import Annotated
# from models import User
# from schemas import CreateUser, UpdateUser
# # Функции работы с записями.
# from sqlalchemy import insert, select, update, delete
# # Функция создания slug-строки
# from slugify import slugify
new = Annotated[Session, Depends(get_db)]

from sqlalchemy import select, update, insert
@router.get("/")
async def all_users(db: new):
    users_all = db.scalars(select(User)).all()
    print('users_all')
    return users_all


@router.post("/create")
async def create_user(db: new, crated_user: CreateUser):
    db.execute(insert(User).values(
        username=crated_user.username,
        firstname=crated_user.firstname,
        lastname=crated_user.lastname,
        age=crated_user.lastname,
        parent_id=crated_user.parent_id,
        slug=slugify(crated_user.username)))

    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put("/update")
async def update_user(db : new, user_id: int, update_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    print(f'aa {user}')
    if user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User is not found'
        )
    db.execute(update(User).where(User.id == user_id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'User update is successful'
    }


@router.delete("/delete")
async def delete_user(db: new, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User is not found'
        )
    db.delete(user)
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'User delete is successful'
    }
