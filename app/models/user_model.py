from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.connection import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    profile_picture = Column(String, nullable=True)
    password = Column(String, nullable=False)
    favorite_plants = relationship("Plant", secondary="user_favorites", back_populates="favorited_by")
