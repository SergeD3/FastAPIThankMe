from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime


class Appreciations(Base):
    appr_text: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created: Mapped[datetime]
