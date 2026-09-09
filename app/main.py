from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(
    title="SmartAI Gateway",
    description="A custom AI Gateway for routing AI requests",
    version="0.1.0",
)

app.include_router(chat_router, prefix="/api/v1")


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "SmartAI Gateway"
    }