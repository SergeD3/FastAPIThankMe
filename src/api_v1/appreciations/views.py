from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import appreciation_by_id

from . import crud
from .schemas import (
    Appreciations,
    AppreciationCreate,
    AppreciationUpdate,
    AppreciationUpdatePartial
)
from src.core.models import db_helper


router = APIRouter(tags=["Appreciations"])


@router.get('/', response_model=list[Appreciations])
async def get_appreciations(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_appreciations(session=session)


@router.post(
    "/",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def create_appreciation(
        appreciation_in: AppreciationCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_appreciation(session=session, appr_in=appreciation_in)


@router.get("/{appreciation_id}/", response_model=Appreciations)
async def get_appreciation(
        appreciation: Appreciations = Depends(appreciation_by_id),
):
    return appreciation


@router.put("/{appreciation_id}/")
async def update_appreciation(
    appreciation_update: AppreciationUpdate,
    appreciation: Appreciations = Depends(appreciation_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_appreciation(
        session=session,
        appreciations=appreciation,
        appreciation_update=appreciation_update,
    )


@router.patch("/{appreciation_id}/")
async def update_user_partial(
    appreciation_update: AppreciationUpdatePartial,
    appreciation: Appreciations = Depends(appreciation_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_appreciation(
        session=session,
        appreciations=appreciation,
        appreciation_update=appreciation_update,
        partial=True,
    )
