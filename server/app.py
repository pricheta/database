from fastapi import FastAPI

from server.models import CreateUserRequest
from database.async_client import create_user_to_db

app = FastAPI(
    docs_url="/api",
    redoc_url=None,
)


@app.get("/")
async def index():
    return {"message": "Hello, World!"}


@app.get("/users/get/{user_id}")
async def get_user(user_id: int):
    return {"message": f"User {user_id} returned"}


@app.post("/users/create/")
async def create_user(request: CreateUserRequest):
    new_user = await create_user_to_db(request=request)
    return {"message": f"User {new_user.id} created"}
