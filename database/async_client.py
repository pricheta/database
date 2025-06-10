from database.engine import session
from database.schemas import User
from server.models import CreateUserRequest


async def create_user_to_db(request: CreateUserRequest) -> User:
    new_user = User(
        email=request.email,
        name=request.name,
        password=request.password,
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user
