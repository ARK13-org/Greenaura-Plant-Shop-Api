from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
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

def get_all_users(db: Session):
    users = db.query(User).all()
    return users

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()

def get_user_by_id(db: Session, user_id: int): 
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user