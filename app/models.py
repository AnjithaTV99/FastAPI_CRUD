from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)



