
from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Form,
    HTTPException,
)
from sqlalchemy.orm import Session
from pathlib import Path
from uuid import uuid4

from app.database import db_plant
from app.database.connection import get_db
from app.schemas.plant import PlantBase, PlantDisplay


router = APIRouter(prefix="/plants", tags=["plants"])

UPLOAD_DIR = Path(__file__).resolve().parents[2] / "uploads" / "plants"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
}

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


@router.post("/", response_model=PlantDisplay)
async def create_plant(
    plant_name: str = Form(...),
    price: float = Form(...),
    category_id: int = Form(...),
    description: str = Form(...),
    size: str | None = Form(None),
    rating: int | None = Form(None),
    humidity: int | None = Form(None),
    temperature: str | None = Form(None),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    extension = Path(image.filename or "").suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG, PNG and WEBP images are allowed",
        )

    if image.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Invalid image type",
        )

    contents = await image.read(MAX_FILE_SIZE + 1)

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="Image must be smaller than 5 MB",
        )

    filename = f"{uuid4().hex}{extension}"
    file_path = UPLOAD_DIR / filename

    image_url = f"/uploads/plants/{filename}"

    file_path.write_bytes(contents)

    try:
        plant = PlantBase(
            plant_name=plant_name,
            price=price,
            category_id=category_id,
            description=description,
            size=size,
            rating=rating,
            humidity=humidity,
            temperature=temperature,
            image_url=image_url,
        )

        return db_plant.create_plant(db, plant)

    except Exception:
        file_path.unlink(missing_ok=True)
        raise

    finally:
        await image.close()


@router.get("/", response_model=list[PlantDisplay])
def get_all_plants(db: Session = Depends(get_db)):
    return db_plant.get_all_plants(db)


@router.delete("/{plant_id}")
def delete_plant(plant_id: int, db: Session = Depends(get_db)):
    db_plant.delete_plant(db, plant_id)
    return {"message": "Plant deleted successfully"}

@router.get("/{plant_id}", response_model=PlantDisplay)
def get_plant(plant_id: int, db: Session = Depends(get_db)):
    return db_plant.get_plant_by_id(db, plant_id)