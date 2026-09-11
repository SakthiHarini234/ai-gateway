from fastapi import APIRouter
from pydantic import BaseModel

from app.gateway.router import GatewayRouter
from app.providers.ollama_provider import OllamaProvider


router = APIRouter()

provider = OllamaProvider()
gateway = GatewayRouter(provider)


class ChatRequest(BaseModel):
    message: str
    model: str = "qwen3:4b"


@router.post("/chat")
async def chat(request: ChatRequest):
    response = await gateway.route(
        request.message,
        request.model
    )

    return {
        "model": request.model,
        "response": response
    }