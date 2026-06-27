from fastapi import FastAPI

from database import SessionLocal
from models import Security
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
