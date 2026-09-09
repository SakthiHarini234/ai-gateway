from app.providers.base import AIProvider


class GatewayRouter:

    def __init__(self, provider: AIProvider):
        self.provider = provider

    async def route(self, message: str) -> str:
        return await self.provider.generate(message)