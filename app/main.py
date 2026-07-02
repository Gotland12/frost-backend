from frost_engine import calculate_f
from frost_engine import calculate_r
from fastapi import FastAPI

from app.database import SessionLocal
from app.models import Security
from sqlalchemy import text


app = FastAPI(title="FROST Backend")

@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/api/v1/securities")
def securities():
    db = SessionLocal()

    result = db.execute(
        text("SELECT ticker, name FROM securities")
    )

    securities = []

    for row in result:
        securities.append({
            "ticker": row.ticker,
            "name": row.name
        })

    db.close()

    return securities

@app.get("/api/v1/frost/{ticker}")
def frost(ticker: str):

    scores = {
        "NVDA": 15,
        "MSFT": 14,
        "ASML": 14,
        "SAP": 12,
        "NOVO-B": 13
    }
f_scores = {
    "NVDA": 3,
    "MSFT": 3,
    "ASML": 3,
    "SAP": 3,
    "NOVO-B": 3


    return {
        "ticker": ticker.upper(),
        "frost_score": scores.get(ticker.upper(), 0),
        "breakdown": {
        "F": 3,
        "R": 3,
        "O": 3,
        "S": 3,
        "T": 3
    }
}
