from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# База данных пользователей
users_db = [
    {"id": 1, "username": "John Doe", "age": 30},
    {"id": 2, "username": "Jane Doe", "age": 25},
]

# Функция для генерации ID
def generate_id():
    return max(user["id"] for user in users_db) + 1

# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Маршрут для создания пользователя
@app.post("/users/", response_class=HTMLResponse)
async def create_user(request: Request, username: str = Form(...), age: int = Form(...)):
    user = {"id": generate_id(), "username": username, "age": age}
    users_db.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})

# Маршрут для чтения пользователей
@app.get("/users/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})

# Маршрут для обновления пользователя
@app.put("/users/{user_id}", response_class=HTMLResponse)
async def update_user(request: Request, user_id: int, username: str = Form(...), age: int = Form(...)):
    for user in users_db:
        if user["id"] == user_id:
            user["username"] = username
            user["age"] = age
            return templates.TemplateResponse("users.html", {"request": request, "users": users_db})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Пользователь не найден"})

# Маршрут для удаления пользователя
@app.delete("/users/{user_id}", response_class=HTMLResponse)
async def delete_user(request: Request, user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            users_db.remove(user)
            return templates.TemplateResponse("users.html", {"request": request, "users": users_db})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Пользователь не найден"})