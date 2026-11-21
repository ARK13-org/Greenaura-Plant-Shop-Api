from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.auth.security import get_current_user
from app.database import db_user
from app.database.connection import get_db
from app.models.user_model import User
from app.schemas.user import UserBase, UserDisplay, UserUpdate
from app.schemas.plant import PlantDisplay

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=UserDisplay, status_code=201)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get("", response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


@router.get("/me/favorites", response_model=list[PlantDisplay])
def get_my_favorites(current_user: User = Depends(get_current_user)):
    return current_user.favorite_plants


@router.patch("/me", response_model=UserDisplay)
def update_my_profile(
    request: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    changes = request.model_dump(exclude_unset=True)
    return db_user.update_user(db, current_user, changes)


@router.get("/{user_id}", response_model=UserDisplay)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(db, user_id)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user.delete_user(db, user_id)
    return {"message": "User deleted successfully."}


UPLOAD_DIR = Path(__file__).resolve().parents[2] / "uploads" / "profile_pictures"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.put("/{user_id}/profile-picture", response_model=UserDisplay)
async def upload_profile_picture(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    user = db_user.get_user_by_id(db, user_id)
    extension = Path(file.filename or "").suffix.lower()
    if file.content_type not in {"image/jpeg", "image/png", "image/webp"} or extension not in {".jpg", ".jpeg", ".png", ".webp"}:
        raise HTTPException(status_code=400, detail="Only JPG, PNG and WEBP images are allowed")
    contents = await file.read(5 * 1024 * 1024 + 1)
    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Image must be smaller than 5 MB")
    filename = f"{uuid4().hex}{extension}"
    (UPLOAD_DIR / filename).write_bytes(contents)
    user.profile_picture = f"/uploads/profile_pictures/{filename}"
    db.commit()
    db.refresh(user)
    await file.close()
    return user
