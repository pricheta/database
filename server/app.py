from fastapi import FastAPI

from server.models import CreateUserRequest
from database.async_client import create_user_to_db, get_user_from_db

app = FastAPI(
    docs_url="/",
    redoc_url=None,
)


@app.get("/users/get/{user_id}")
async def get_user(user_id: int):
    return await get_user_from_db(user_id=user_id)


@app.post("/users/create/")
async def create_user(request: CreateUserRequest):
    new_user = await create_user_to_db(request=request)
    return {"message": f"User {new_user.id} created"}
