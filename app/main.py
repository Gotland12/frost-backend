from fastapi import FastAPI

app = FastAPI(title="FROST Backend")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/api/v1/securities")
def securities():
    return [
        {"ticker": "NVDA", "name": "NVIDIA"},
        {"ticker": "MSFT", "name": "Microsoft"},
        {"ticker": "ASML", "name": "ASML"},
        {"ticker": "SAP", "name": "SAP"}
    ]
