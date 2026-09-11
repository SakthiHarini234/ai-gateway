from app.providers.base import AIProvider


class GatewayRouter:

    def __init__(self, provider: AIProvider):
        self.provider = provider

    async def route(self, message: str, model: str | None = None) -> str:
        if model:
            self.provider.model = model

        return await self.provider.generate(message)