from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import db_user
from app.database.connection import get_db
from app.schemas.user import UserBase, UserDisplay
from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile, File, HTTPException

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

@router.get("", response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

@router.get("/{user_id}", response_model=UserDisplay)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(db, user_id)

@router.delete("/{user_id}", status_code=200)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user.delete_user(db, user_id)
    return {"message": "User deleted successfully."}

UPLOAD_DIR = Path("uploads/profile_pictures")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.put("/{user_id}/profile-picture", response_model=UserDisplay)
async def upload_profile_picture(
    user_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    allowed_types = ["image/jpeg", "image/png", "image/webp"]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, PNG, and WEBP images are allowed."
        )

    user = db_user.get_user_by_id(db, user_id)

    extension = Path(file.filename or "").suffix.lower()

    if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
        raise HTTPException(status_code=400, detail="Invalid image extension.")

    filename = f"{uuid4().hex}{extension}"
    file_path = UPLOAD_DIR / filename

    with file_path.open("wb") as image:
        image.write(await file.read())

    user.profile_picture = f"/uploads/profile_pictures/{filename}"

    db.commit()
    db.refresh(user)

    return user