from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import db_user
from app.database.connection import get_db
from app.schemas.user import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
