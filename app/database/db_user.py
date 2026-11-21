from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.hash import Hash
from app.models.user_model import User
from app.schemas.user import UserBase


def create_user(db: Session, request: UserBase) -> User:
    if db.query(User).filter(User.username == request.username).first():
        raise HTTPException(status_code=409, detail="Username already exists")
    if db.query(User).filter(User.email == str(request.email)).first():
        raise HTTPException(status_code=409, detail="Email already exists")
    user = User(
        username=request.username, name=request.name, last_name=request.last_name,
        phone_number=request.phone_number, email=str(request.email),
        password=Hash.hash_password(request.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session):
    return db.query(User).all()


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()


def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def update_user(db: Session, user: User, changes: dict) -> User:
    email = changes.get("email")
    if email and email != user.email:
        existing = db.query(User).filter(User.email == email, User.id != user.id).first()
        if existing:
            raise HTTPException(status_code=409, detail="Email already exists")
    for field, value in changes.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user
