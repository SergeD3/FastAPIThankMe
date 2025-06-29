import uvicorn

from contextlib import asynccontextmanager
from src.core.config import settings
from src.api_v1 import router as router_v1
from src.core.models import Base, db_helper
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

@app.get("/appreciations", tags=["Appreciations"])
async def get_appreciations_by_user():
    return {"message": "get_appreciations_by_user"}


@app.get("/feedback", tags=["Feedbacks"])
async def get_feedbacks_by_user():
    return {"message": "get_feedbacks_by_user"}

@app.get("/", tags=["Home"])
async def home():
    return {"message": "home"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)