import fastapi
from typing import List
from models.users_model import User

router = fastapi.APIRouter()


users = []


@router.get("/users", response_model=List[User])
async def read_items():
    return users


@router.post("/users", response_model=User)
async def create_user(user: User):
    users.append(user)
    return user


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    users[user_id] = user
    return user


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    del users[user_id]
    return {"message": "User deleted"}
