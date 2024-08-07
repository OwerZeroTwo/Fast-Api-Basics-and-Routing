from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}
last_id = 1

@app.get("/users")
async def get_users():
    return JSONResponse(users)

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    global last_id
    last_id += 1
    users[str(last_id)] = f"Имя: {username}, возраст: {age}"
    return JSONResponse(f"User {last_id} is registered")

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    if str(user_id) in users:
        users[str(user_id)] = f"Имя: {username}, возраст: {age}"
        return JSONResponse(f"The user {user_id} is registered")
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    if str(user_id) in users:
        del users[str(user_id)]
        return JSONResponse(f"User {user_id} has been deleted")
    else:
        raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
