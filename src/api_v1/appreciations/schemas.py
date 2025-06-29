from datetime import datetime
from pydantic import BaseModel, ConfigDict


class AppreciationsBase(BaseModel):
    message: str
    to_: int
    from_: int
    date_created: datetime


class Appreciations(AppreciationsBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class AppreciationCreate(AppreciationsBase):
    pass


class AppreciationUpdate(AppreciationsBase):
    pass


class AppreciationUpdatePartial(AppreciationsBase):
    message: str | None = None
    to_: int | None = None
    from_: int | None = None
    date_created: datetime = datetime.now()
