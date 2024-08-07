from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int

users = []

# GET запрос по маршруту '/users'
@app.get("/users")
def get_users():
    return users

# POST запрос по маршруту '/user/{username}/{age}'
@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    user_id = len(users) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

# PUT запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос по маршруту '/user/{user_id}'
@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")