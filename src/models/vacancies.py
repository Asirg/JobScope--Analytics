from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

import datetime


class Sources(Base):
    __tablename__ = 'sources'

    source_id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    link: Mapped[str]

    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[datetime.datetime]