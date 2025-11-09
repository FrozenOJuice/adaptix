from fastapi import FastAPI

app = FastAPI(title="Adaptix API")

@app.get("/")
def root():
    return {"message": "Adaptix backend initialized successfully"}
