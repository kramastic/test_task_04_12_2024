from sqlalchemy import ForeignKey
from app.baskets.models import Baskets
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Mushrooms(Base):
    __tablename__ = "mushrooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    eatable: Mapped[bool] = mapped_column(nullable=False)
    weight: Mapped[int] = mapped_column(nullable=False)
    freshness: Mapped[bool] = mapped_column(nullable=False)

    basket_id: Mapped[int] = mapped_column(ForeignKey("baskets.id"))
    basket: Mapped[Baskets] = relationship("Baskets", back_populates="mushrooms")

