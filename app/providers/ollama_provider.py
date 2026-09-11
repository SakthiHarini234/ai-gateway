from ollama import AsyncClient

from app.providers.base import AIProvider


class OllamaProvider(AIProvider):

    def __init__(self, model: str = "qwen3:4b"):
        self.model = model
        self.client = AsyncClient()

    async def generate(self, message: str) -> str:
        response = await self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]