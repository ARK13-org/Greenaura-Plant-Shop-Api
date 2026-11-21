from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.database.connection import Base, engine
from app import models
from app.routers import user, category, plant, auth

# Creates newly introduced tables while preserving existing catalogue and user data.
Base.metadata.create_all(bind=engine)

UPLOAD_ROOT = Path(__file__).resolve().parent.parent / "uploads"
(UPLOAD_ROOT / "plants").mkdir(parents=True, exist_ok=True)
(UPLOAD_ROOT / "profile_pictures").mkdir(parents=True, exist_ok=True)

app = FastAPI(title=settings.APP_NAME, description="REST API for the GreenAura Plant Shop", version="1.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:2350", "http://127.0.0.1:2350"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router)
app.include_router(category.router)
app.include_router(plant.router)
app.include_router(auth.router)
app.mount("/uploads", StaticFiles(directory=str(UPLOAD_ROOT)), name="uploads")


@app.get("/")
def root():
    return {"message": "Welcome to GreenAura API!", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
