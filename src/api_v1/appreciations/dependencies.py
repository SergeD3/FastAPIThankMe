from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.appreciations import crud
from src.core.models import db_helper, Appreciations


async def appreciation_by_id(
        appreciation_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Appreciations:
    appreciation = await crud.get_appreciation_by_id(
        session=session,
        appr_id=appreciation_id,
    )

    if appreciation:
        return appreciation

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Appreciation not found",
    )
