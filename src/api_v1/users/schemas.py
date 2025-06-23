from pydantic import BaseModel, ConfigDict


class UsersBase(BaseModel):
    name: str
    position: str
    telegram_username: str


class UserCreate(UsersBase):
    pass


class Users(UsersBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):
    name: str | None = None
    position: str | None = None
    telegram_username: str | None = None
