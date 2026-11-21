from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: str
    name: str
    last_name: str
    phone_number: str | None = None
    email: EmailStr
    password: str


class UserDisplay(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    name: str
    last_name: str
    phone_number: str | None = None
    email: EmailStr
    profile_picture: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserUpdate(BaseModel):
    name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    email: EmailStr | None = None
