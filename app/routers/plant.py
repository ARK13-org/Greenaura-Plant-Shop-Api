from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.auth.security import get_current_user
from app.database import db_plant
from app.database.connection import get_db
from app.models.plant_model import Plant
from app.models.category_model import Category
from app.models.user_model import User
from app.schemas.plant import PlantBase, PlantDisplay, FavoriteUpdate

router = APIRouter(prefix="/plants", tags=["plants"])
UPLOAD_DIR = Path(__file__).resolve().parents[2] / "uploads" / "plants"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE = 5 * 1024 * 1024


@router.get("/", response_model=list[PlantDisplay])
def get_all_plants(
    category_id: int | None = Query(default=None),
    search: str | None = Query(default=None, min_length=1, max_length=100),
    db: Session = Depends(get_db),
):
    query = db.query(Plant)
    if category_id is not None:
        query = query.filter(Plant.category_id == category_id)
    if search and search.strip():
        term = f"%{search.strip()}%"
        query = query.filter(or_(Plant.plant_name.ilike(term), Plant.description.ilike(term), Plant.category.has(Category.name.ilike(term))))
    return query.order_by(Plant.id.asc()).all()


@router.get("/{plant_id}", response_model=PlantDisplay)
def get_plant(plant_id: int, db: Session = Depends(get_db)):
    return db_plant.get_plant_by_id(db, plant_id)


@router.put("/{plant_id}/favorite")
def update_favorite(
    plant_id: int, request: FavoriteUpdate,
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user),
):
    plant = db_plant.get_plant_by_id(db, plant_id)
    if request.is_favorite and plant not in current_user.favorite_plants:
        current_user.favorite_plants.append(plant)
    elif not request.is_favorite and plant in current_user.favorite_plants:
        current_user.favorite_plants.remove(plant)
    db.commit()
    return {"plant_id": plant_id, "is_favorite": request.is_favorite}


@router.post("/", response_model=PlantDisplay)
async def create_plant(
    plant_name: str = Form(...), price: float = Form(...), category_id: int = Form(...),
    description: str = Form(...), size: str | None = Form(None), rating: float | None = Form(None),
    humidity: int | None = Form(None), temperature: str | None = Form(None),
    image: UploadFile = File(...), db: Session = Depends(get_db),
):
    extension = Path(image.filename or "").suffix.lower()
    if extension not in ALLOWED_EXTENSIONS or image.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="Only JPG, PNG and WEBP images are allowed")
    contents = await image.read(MAX_FILE_SIZE + 1)
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Image must be smaller than 5 MB")
    filename = f"{uuid4().hex}{extension}"
    file_path = UPLOAD_DIR / filename
    image_url = f"/uploads/plants/{filename}"
    file_path.write_bytes(contents)
    try:
        plant = PlantBase(
            plant_name=plant_name, price=price, category_id=category_id,
            description=description, size=size, rating=rating, humidity=humidity,
            temperature=temperature, image_url=image_url,
        )
        return db_plant.create_plant(db, plant)
    except Exception:
        file_path.unlink(missing_ok=True)
        raise
    finally:
        await image.close()


@router.delete("/{plant_id}")
def delete_plant(plant_id: int, db: Session = Depends(get_db)):
    db_plant.delete_plant(db, plant_id)
    return {"message": "Plant deleted successfully"}
