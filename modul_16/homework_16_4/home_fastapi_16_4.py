from fastapi import FastAPI, Path, HTTPException, Body
from typing import Annotated
from pydantic import BaseModel
from typing import List

app = FastAPI()

User_db = []


class User(BaseModel):
    id: int
    username: str
    age: int






# get запрос по маршруту '/users' теперь возвращает список users.
@app.get("/users")
async def get_all_messages() -> List[User]:
    return User_db


# post запрос по маршруту '/user/{username}/{age}', теперь:
# Добавляет в список users объект User.
# id этого объекта будет на 1 больше, чем у последнего в списке users.
# Если список users пустой, то 1.
# Все остальные параметры объекта
# User - переданные в функцию username и age соответственно.
# В конце возвращает созданного пользователя.


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
async def update_message(new_id: int, username: str, age: int) -> str:
    try:
        result = [item for item in User_db if item.id == new_id]
        result[0].username = username
        result[0].age = age
        return 'User update'
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}')
async def delete_message(user_id: int) -> str:
    try:
        for item in User_db:
            if item.id == 2:
                User_db.remove(item)
                break
        print(User_db)
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')
