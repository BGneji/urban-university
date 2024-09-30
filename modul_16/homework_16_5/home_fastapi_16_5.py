import fastapi
from fastapi import FastAPI, Path, HTTPException, Body, status, Request, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel
from typing import List
# импортируем Jinja2Templates
from fastapi.templating import Jinja2Templates

app = FastAPI()

User_db = []

templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int
    username: str
    age: int


# Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html',
# а также передавать в него request и список users. Ключи в словаре
# для передачи определите самостоятельно в соответствии с шаблоном.

@app.get("/")
async def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": User_db})


# Измените get запрос по маршруту '/users' на '/users/{user_id}':
# Функция по этому запросу теперь принимает аргумент request и user_id.
# Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html',
# а также передавать в него request и одного из пользователей - user.
# Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.


@app.get("/users/{user_id}")
async def get_all_messages(request: Request, user_id: int) -> HTMLResponse:
    try:
        user_id = user_id - 1
        return templates.TemplateResponse("users.html", {"request": request, "users_one": User_db[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.post("/user/{username}/{age}")
async def name_age_page(username: str, age: int) -> str:
    new_id = len(User_db) + 1
    new_user = User(id=new_id, username=username, age=age)
    User_db.append(new_user)
    return f'User created {new_user}'


# put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
# Обновляет username и age пользователя, если пользователь
# с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение
# HTTPException с описанием "User was not found" и кодом 404.
@app.put("/user/{user_id}/{username}/{age}")
# async def update_message(new_id: int, username: str, age: int) -> str:
async def update_message(user: User) -> str:
    try:
        result = [item for item in User_db if item.id == user.id]
        result[0].username = user.username
        result[0].age = user.age
        return 'User update'
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}')
async def delete_message(user_id: int) -> str:
    try:
        for user in User_db:
            if user.id == 2:
                User_db.remove(user)
                break
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')
