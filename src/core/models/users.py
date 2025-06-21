from .base import Base
from sqlalchemy.orm import Mapped


class Users(Base):
    name: Mapped[str]
    position: Mapped[str]
    telegram_username: Mapped[str]
