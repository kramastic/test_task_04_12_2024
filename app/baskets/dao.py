from app.baskets.models import Baskets
from app.baskets.schemas import SResponseBaskets
from app.database import async_session_maker
from sqlalchemy import and_, delete, insert, select, update
from app.mushrooms.models import Mushrooms
from app.mushrooms.schemas import SResponseMushrooms


class BasketsDAO:
    model = Baskets

    @classmethod
    async def add_basket(cls, **data):
        async with async_session_maker() as session:
            query = insert(Baskets).values(**data).returning(Baskets)
            new_basket = await session.execute(query)
            await session.commit()
            return new_basket.scalar()
    
    @classmethod
    async def get_basket(cls, id):
        async with async_session_maker() as session:

            query_basket = select(Baskets).filter_by(id=id)
            result_basket = await session.execute(query_basket)
            basket_validate = SResponseBaskets.model_validate(result_basket.scalar()).model_dump()

            query_mushrooms = select(Mushrooms).where(Mushrooms.basket_id == id)
            result_mushrooms = await session.execute(query_mushrooms)
            mushrooms_validate =  [SResponseMushrooms.model_validate(row, from_attributes=True) for row in result_mushrooms.scalars().all()]

            basket_validate["mushrooms"] = mushrooms_validate

            return basket_validate
        
    @classmethod
    async def add_mushroom(cls, mushroom_id, basket_id):
        async with async_session_maker() as session:
            query = update(Mushrooms).where(Mushrooms.id==mushroom_id).values(basket_id=basket_id)
            await session.execute(query)
            await session.commit()
            return True
            
    @classmethod
    async def delete_mushroom(cls, mushroom_id, basket_id):
        async with async_session_maker() as session:
            query_delete = delete(Mushrooms).where(
                and_(Mushrooms.id == mushroom_id, Mushrooms.basket_id == basket_id))
            await session.execute(query_delete)
            await session.commit()
            return True
