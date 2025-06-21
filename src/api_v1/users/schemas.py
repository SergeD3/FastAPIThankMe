from pydantic import BaseModel, ConfigDict


class UsersBase(BaseModel):
    name: str
    position: str
    telegram_username: str


class UsersCreate(BaseModel):
    pass


class Users(UsersBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
