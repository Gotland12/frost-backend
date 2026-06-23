from fastapi import FastAPI

app = FastAPI(title="FROST Backend")

@app.get("/")
def root():
    return {"status": "ok"}
  
