from pydantic import BaseModel

# CreateUser с атрибутами: username(str), firstname(str), lastname(str) и age(int)
# UpdateUser с атрибутами: firstname(str), lastname(str) и age(int)
# CreateTask с атрибутами: title(str), content(str), priority(int)
# UpdateTask с теми же атрибутами, что и CreateTask.

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateTask(BaseModel):
    title: str
    content: str
    priority: str

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: str

