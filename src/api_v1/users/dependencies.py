from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.users import crud
from src.core.models import db_helper, Users


async def user_by_id(
        user_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Users:
    user = await crud.get_user_by_id(session=session, user_id=user_id)

    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )
