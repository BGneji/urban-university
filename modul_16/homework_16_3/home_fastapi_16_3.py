from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

messages_db = {1: 'Имя: Example, возраст: 18'}


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/users")
async def get_all_messages() -> dict:
    return messages_db


@app.post("/user/{username}/{age}")
async def name_age_page(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                      example='UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    current_index = int(int(max(messages_db, key=int)) + 1)
    messages_db[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: int, username: str, age: int) -> str:
    messages_db[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is registered"


@app.delete('/user/{user_id}')
async def delete_message(user_id: int) -> str:
    messages_db.pop(user_id)
    return f"User {user_id} has been deleted"
