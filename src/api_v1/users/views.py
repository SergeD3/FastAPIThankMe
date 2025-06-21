from itertools import product

from fastapi import APIRouter, HTTPException, status
from . import crud
from .schemas import Users, UsersCreate


router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[Users])
async def get_users(session):
    return await crud.get_users(session=session)


@router.post("/", response_model=Users)
async def create_user(session, user_in: UsersCreate):
    return await crud.create_user(session=session, user_in=user_in)


@router.get("/{user_id}/", response_model=Users)
async def get_user(user_id: int, session):
    user = await crud.get_user_by_id(session=session, user_id=user_id)

    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

