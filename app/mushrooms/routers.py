from fastapi import APIRouter
from app.mushrooms.dao import MushroomsDAO
from app.mushrooms.schemas import SAddMushrooms, SResponseMushrooms, SUpdateMushrooms


router = APIRouter(
    prefix="/mushrooms",
    tags=["Mushrooms"]
)


@router.post("/add_mushroom")
async def add_basket(mushrooms_data: SAddMushrooms):
    new_mushroom = await MushroomsDAO.add_mushroom(
        title=mushrooms_data.title, 
        eatable=mushrooms_data.eatable,
        weight=mushrooms_data.weight,
        freshness=mushrooms_data.freshness,
        basket_id=mushrooms_data.basket_id
        )
    return new_mushroom

@router.get("/get_mushroom")
async def get_mushroom(id: int):
    mushroom = await MushroomsDAO.get_mushroom(id=id)
    return mushroom

@router.put("/update_info")
async def update_mushroom(
        id: int,
        title: str,
        eatable: bool,
        weight: int,
        freshness: bool 
        ):
    data = {"title":title, "eatable":eatable, "weight":weight, "freshness":freshness}
    updated_mushrooms = await MushroomsDAO.update_mushroom(id, data)
    return updated_mushrooms



