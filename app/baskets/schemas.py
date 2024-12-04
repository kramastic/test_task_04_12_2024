from typing import List
from pydantic import BaseModel, ConfigDict
from app.mushrooms.schemas import SResponseMushrooms


class SAddBaskets(BaseModel):
    owner: str
    capacity: int

    model_config = ConfigDict(from_attributes=True)

class SResponseBaskets(SAddBaskets):
    id: int



