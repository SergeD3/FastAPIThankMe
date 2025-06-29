from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime


class Appreciations(Base):
    message: Mapped[str]
    from_: Mapped[int] = mapped_column(ForeignKey('users.id'))
    to_: Mapped[int] = mapped_column(ForeignKey('users.id'))
    date_created: Mapped[datetime]
