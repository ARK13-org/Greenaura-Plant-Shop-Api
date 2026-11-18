from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    name: str
    last_name: str
    phone_number: str
    email: str
    password: str


class UserDisplay(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str
    name: str
    last_name: str
    phone_number: str
    email: str
