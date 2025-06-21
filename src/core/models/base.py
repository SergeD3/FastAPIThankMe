from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstraact__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
