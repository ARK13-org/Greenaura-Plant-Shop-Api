from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import db_category
from app.database.connection import get_db
from app.database import db_category
from app.schemas.category import CategoryBase, CategoryDisplay

router = APIRouter(prefix="/category", tags=["category"])

@router.post("", response_model=CategoryDisplay)
def create_category(request: CategoryBase, db: Session = Depends(get_db)):
    return db_category.create_category(db, request)

@router.get("", response_model=list[CategoryDisplay])
def get_all_categories(db: Session = Depends(get_db)):
    return db_category.get_all_categories(db)

@router.delete("/{category_id}", status_code=200)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category.delete_category(db, category_id)
    return {"message": "Category deleted successfully."}