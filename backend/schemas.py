from pydantic import BaseModel
from datetime import datetime

class PredictionInput(BaseModel):
    platform: str
    genre: str
    year: int

class PredictionOutput(BaseModel):
    predicted_sales: float
    platform: str
    genre: str
    year: int

class PredictionRecord(BaseModel):
    id: int
    platform: str
    genre: str
    year: int
    predicted_sales: float
    created_at: datetime

    class Config:
        from_attributes = True