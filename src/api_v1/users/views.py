from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from . import crud
from .schemas import Users, UserCreate, UserUpdate, UserUpdatePartial
from src.core.models import db_helper
from .dependencies import user_by_id


router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[Users])
async def get_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_users(session=session)


@router.post("/", response_model=Users)
async def create_user(
        user_in: UserCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_user(session=session, user_in=user_in)


@router.get("/{user_id}/", response_model=Users)
async def get_user(
        user: Users = Depends(user_by_id),
):
    return user

@router.put("/{user_id}/")
async def update_user(
    user_update: UserUpdate,
    user: Users = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )
