"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.models import Appreciations
from .schemas import (
    AppreciationCreate,
    AppreciationUpdate,
    AppreciationUpdatePartial
)


async def get_appreciations(session: AsyncSession) -> list[Appreciations]:
    stmt = select(Appreciations).order_by(Appreciations.id)
    result: Result = await session.execute(stmt)
    appreciations = result.scalars().all()

    return list(appreciations)


async def get_appreciation_by_id(session: AsyncSession, appr_id: int) -> Appreciations | None:
    return await session.get(Appreciations, appr_id)


async def create_appreciation(session: AsyncSession, appr_in: AppreciationCreate) -> Appreciations:
    appreciation = Appreciations(**appr_in.model_dump())
    session.add(appreciation)
    await session.commit()
    await session.refresh(appreciation)

    return appreciation


async def update_appreciation(
        session: AsyncSession,
        appreciations: Appreciations,
        appreciation_update: AppreciationUpdate | AppreciationUpdatePartial,
        partial: bool = False,
) -> Appreciations:
    for name, value in appreciation_update.model_dump(exclude_unset=partial).items():
        setattr(appreciations, name, value)

    await session.commit()
    return appreciations

async def delete_appreciation(
        session: AsyncSession,
        appreciation: Appreciations
) -> None:
    await session.delete(appreciation)
    await session.commit()
