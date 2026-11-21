from sqlalchemy import Column, ForeignKey, Integer, Table
from app.database.connection import Base

user_favorites = Table(
    "user_favorites",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True),
    Column("plant_id", Integer, ForeignKey("plant.id", ondelete="CASCADE"), primary_key=True),
)
