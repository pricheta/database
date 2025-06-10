from fastapi import FastAPI

from models import CreateUserRequest


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
    return {"message": f"User created from request: {request}"}
