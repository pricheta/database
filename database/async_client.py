from sqlalchemy import select

from database.engine import session
from database.schemas import User
from server.models import CreateUserRequest


async def get_user_from_db(user_id: int) -> User:
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)
    user = result.scalars().first()
    return user


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
