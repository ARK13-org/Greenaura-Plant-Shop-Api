from fastapi import FastAPI

from app.core.config import settings
from app.routers import user
from app.routers import category

app = FastAPI(
    title=settings.APP_NAME,
    description="REST API for the GreenAura Plant Shop",
    version="1.0.0",
)

app.include_router(user.router)
app.include_router(category.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to GreenAura API!",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
