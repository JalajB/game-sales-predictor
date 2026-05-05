from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String)
    genre = Column(String)
    year = Column(Integer)
    predicted_sales = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())