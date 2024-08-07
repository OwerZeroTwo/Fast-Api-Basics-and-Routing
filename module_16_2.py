from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/{user_id}")
async def read_user(
    user_id: Annotated[int, Path(title="Enter User ID", description="User ID", ge=1, le=100, example=1)]
):
    return {"user_id": user_id}

@app.get("/user/{username}/{age}")
async def read_user(
    username: Annotated[str, Path(title="Enter username", description="Username", min_length=5, max_length=20, example="UrbanUser")],
    age: Annotated[int, Path(title="Enter age", description="Age", ge=18, le=120, example=24)]
):
    return {"username": username, "age": age}