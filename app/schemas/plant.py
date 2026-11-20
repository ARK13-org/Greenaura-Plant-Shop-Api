
from pydantic import BaseModel, ConfigDict


class CategoryInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class PlantBase(BaseModel):
    plant_name: str
    price: float
    size: str | None = None
    rating: float | None = None
    humidity: int | None = None
    temperature: str | None = None
    category_id: int
    image_url: str
    description: str


class PlantDisplay(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    plant_name: str
    price: float
    size: str | None = None
    rating: float | None = None
    humidity: int | None = None
    temperature: str | None = None
    category: CategoryInfo
    image_url: str
    description: str
