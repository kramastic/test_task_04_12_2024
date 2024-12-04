from pydantic import BaseModel, ConfigDict

class SUpdateMushrooms(BaseModel):
    title: str
    eatable: bool
    weight: int
    freshness: bool

    model_config = ConfigDict(from_attributes=True)

class SAddMushrooms(SUpdateMushrooms):
    basket_id: int

class SResponseMushrooms(SAddMushrooms):
    id: int


