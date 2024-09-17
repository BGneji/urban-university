from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": f"Вы вошли как администратор"}


@app.get('/user/{user_id}')
async def user_id_page(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def name_age_page(username: str, age: int) -> dict:
    return {"message": f"Hello {username} {age}"}
