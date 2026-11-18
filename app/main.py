
from fastapi import FastAPI, Path

from app.core.config import settings
from app.database.connection import Base, engine
from app import models
from app.routers import user, category , plant
from fastapi.staticfiles import StaticFiles
from pathlib import Path


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="REST API for the GreenAura Plant Shop",
    version="1.0.0",
)

app.include_router(user.router)
app.include_router(category.router)
app.include_router(plant.router)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

UPLOAD_ROOT = Path(__file__).resolve().parent.parent / "uploads"
UPLOAD_ROOT.mkdir(parents=True, exist_ok=True)

app.mount(
    "/uploads",
    StaticFiles(directory=str(UPLOAD_ROOT)),
    name="uploads",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to GreenAura API!",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
