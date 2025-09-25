from fastapi import FastAPI
from .routes import soil_routes

app = FastAPI(title="Crop Soil API", version="1.0")

app.include_router(soil_routes.router)

@app.get("/")
def root():
    return {"message": "🌱 Crop Soil API is running"}
