# plantation category database operations
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from app.models.category_model import Category
from app.schemas.category import CategoryBase

def create_category(db: Session, category_name: str):
    category = Category(name=category_name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_all_categories(db: Session):
    categories = db.query(Category).all()
    return categories

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    db.delete(category)
    db.commit()