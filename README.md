# Game Sales Predictor

A full-stack ML web app that predicts video game global sales (in millions of units) based on platform, genre, and release year.

Built as a learning project from scratch — no shortcuts, no copy-paste without understanding.

---

## What it does

- User inputs a game's platform, genre, and year
- A trained Linear Regression model predicts how many units it will sell globally
- Every prediction is stored in a PostgreSQL database
- History of all predictions is shown below the form

---

## Tech Stack

| Layer | Technology |
|---|---|
| ML Model | Linear Regression from scratch using NumPy only |
| Data | Pandas (cleaning + feature engineering) |
| Visualization | Matplotlib (loss curves) |
| Backend | FastAPI + Uvicorn |
| Validation | Pydantic |
| Database | PostgreSQL + SQLAlchemy |
| Frontend | React |
| Containerization | Docker + Docker Compose |
| Deployment | Render (free tier) |

---

## How it works

### ML Pipeline
- Dataset: [Video Game Sales — Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales) (~16,000 games)
- Cleaned missing values, dropped irrelevant columns
- One-hot encoded `Platform` and `Genre`
- Applied `log1p` transform on `Global_Sales` to handle skewed distribution
- Normalized features and target using mean/std
- Trained Linear Regression using Gradient Descent (NumPy only, no sklearn)
- Saved weights as `.npy` files — loaded by the backend at runtime

### Backend
- FastAPI serves two endpoints:
  - `POST /predict` — runs the model and stores result in DB
  - `GET /history` — returns all past predictions
- Pydantic validates all incoming requests
- SQLAlchemy ORM handles all database operations

### Frontend
- Minimal React UI
- User fills in platform, genre, year → hits Predict
- Calls the FastAPI backend, displays result and history table

### Docker
- Three containers: backend, frontend, PostgreSQL
- `docker-compose.yml` orchestrates all three
- PostgreSQL data persists via a named volume

### Deployment
- Backend and frontend deployed separately on Render free tier
- PostgreSQL hosted on Render's managed database (free tier)

---

## Project Structure

```
game-sales-predictor/
├── ml/
│   ├── explore.py
│   ├── clean.py
│   ├── features.py
│   ├── train.py
│   └── vgsales_clean.csv
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── weights.npy (+ other .npy files)
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.css
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## What I learned

- Linear Regression from first principles — forward pass, MSE loss, gradient descent, weight updates
- Why normalization and log transforms matter in real data
- One-hot encoding and why integer encoding is wrong for categorical data
- How FastAPI, Pydantic, SQLAlchemy, and PostgreSQL fit together
- How Docker containers work, what images are, and how docker-compose ties services together
- How to deploy a full-stack app on Render with environment variables

---

## Built with help from

This project was built with step-by-step guidance from [Claude](https://claude.ai) (Anthropic's AI assistant). Every concept was explained from first principles before any code was written. The goal was deep understanding, not just shipping — and Claude made that possible.

