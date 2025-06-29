from fastapi import APIRouter

from .users.views import router as users_router
from .appreciations.views import router as appreciations_router


router = APIRouter()
router.include_router(router=users_router, prefix="/users")
router.include_router(router=appreciations_router, prefix="/appreciations")
