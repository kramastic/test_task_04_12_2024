from fastapi import APIRouter
from sqlalchemy import update
from app.baskets.dao import BasketsDAO
from app.baskets.schemas import SAddBaskets, SResponseBaskets


router = APIRouter(
    prefix="/baskets",
    tags=["Baskets"]
)


@router.post("/add_basket")
async def add_basket(basket_data: SAddBaskets):
    new_basket = await BasketsDAO.add_basket(owner=basket_data.owner, capacity=basket_data.capacity)
    return new_basket

@router.get("/get_basket")
async def get_basket(id: int):
    basket = await BasketsDAO.get_basket(id=id)
    return basket

@router.post("/add_mushroom")
async def add_mushroom(mushroom_id: int, basket_id: int):
    await BasketsDAO.add_mushroom(mushroom_id=mushroom_id, basket_id=basket_id)
    return f"Гриб id_{mushroom_id} добавлен в корзину id_{basket_id}."

@router.delete("/delete")
async def delete_mushroom(mushroom_id: int, basket_id: int):
    await BasketsDAO.delete_mushroom(mushroom_id=mushroom_id, basket_id=basket_id)
    return f"Гриб id_{mushroom_id} выброшен."