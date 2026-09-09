from fastapi import APIRouter
from pydantic import BaseModel

from app.gateway.router import GatewayRouter
from app.providers.mock_provider import MockProvider


router = APIRouter()

provider = MockProvider()
gateway = GatewayRouter(provider)


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):
    response = await gateway.route(request.message)

    return {
        "response": response
    }