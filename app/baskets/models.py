from typing import List
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Baskets(Base):
    __tablename__ = "baskets"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(nullable=False)
    capacity: Mapped[int] = mapped_column(nullable=False)

    mushrooms = relationship("Mushrooms", back_populates="basket")



