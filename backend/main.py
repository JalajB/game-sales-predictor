from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
import models, schemas
from model import predict

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict", response_model=schemas.PredictionOutput)
def make_prediction(input: schemas.PredictionInput, db: Session = Depends(get_db)):
    result = predict(input.platform, input.genre, input.year)

    record = models.Prediction(
        platform=input.platform,
        genre=input.genre,
        year=input.year,
        predicted_sales=result
    )
    db.add(record)
    db.commit()

    return schemas.PredictionOutput(
        predicted_sales=result,
        platform=input.platform,
        genre=input.genre,
        year=input.year
    )

@app.get("/history", response_model=list[schemas.PredictionRecord])
def get_history(db: Session = Depends(get_db)):
    return db.query(models.Prediction).order_by(models.Prediction.created_at.desc()).all()