from sqlalchemy.orm import Session

from app.database.hash import Hash
from app.models.user_model import User
from app.schemas.user import UserBase


def create_user(db: Session, request: UserBase) -> User:
    user = User(
        username=request.username,
        name=request.name,
        last_name=request.last_name,
        phone_number=request.phone_number,
        email=request.email,
        password=Hash.hash_password(request.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user