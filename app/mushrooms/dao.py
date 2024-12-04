from app.baskets.models import Baskets
from app.database import async_session_maker
from sqlalchemy import insert, select, update
from app.mushrooms.models import Mushrooms
from app.mushrooms.schemas import SResponseMushrooms


class MushroomsDAO:
    model = Baskets

    @classmethod
    async def add_mushroom(cls, **data):
        async with async_session_maker() as session:
            query = insert(Mushrooms).values(**data).returning(Mushrooms)
            new_mushroom = await session.execute(query)
            await session.commit()
            new_mushroom_validate = SResponseMushrooms.model_validate(new_mushroom.scalar()).model_dump()
            return new_mushroom_validate
        
    @classmethod
    async def get_mushroom(cls, id):
        async with async_session_maker() as session:
            query = select(Mushrooms).filter_by(id=id)
            mushroom = await session.execute(query)
            mushroom_validate = SResponseMushrooms.model_validate(mushroom.scalar_one_or_none()).model_dump()
            return mushroom_validate
        
    @classmethod
    async def update_mushroom(cls, id, data):
        async with async_session_maker() as session:
            query = update(Mushrooms).where(Mushrooms.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            return f"Данные гриба id_{id} обновлены."




