
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Plant(Base):
    __tablename__ = "plant"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Numeric(10, 2), nullable=False)
    size = Column(String)
    rating = Column(Integer)
    humidity = Column(Integer)
    temperature = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))
    plant_name = Column(String, nullable=False)
    image_url = Column(String)
    description = Column(String)

    category = relationship("Category", back_populates="plants")