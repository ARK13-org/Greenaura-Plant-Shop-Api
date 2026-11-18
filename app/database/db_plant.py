
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from app.database.hash import Hash
from app.models.plant_model import Plant
from app.schemas.plant import PlantBase

def create_plant(db: Session, plant: PlantBase):
    new_plant = Plant(**plant.model_dump())

    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)

    return new_plant


def get_all_plants(db: Session):
    return db.query(Plant).all()

def get_plant_by_id(db: Session, plant_id: int):
    plant = db.query(Plant).filter(Plant.id == plant_id).first()

    if not plant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plant not found"
        )

    return plant


def delete_plant(db: Session, plant_id: int):
    plant = db.query(Plant).filter(Plant.id == plant_id).first()

    if not plant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plant not found"
        )

    db.delete(plant)
    db.commit()

    return {"message": "Plant deleted successfully"}
