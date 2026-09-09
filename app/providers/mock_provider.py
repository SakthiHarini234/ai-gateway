from app.providers.base import AIProvider


class MockProvider(AIProvider):

    async def generate(self, message: str) -> str:
        return f"Gateway received your request: {message}"