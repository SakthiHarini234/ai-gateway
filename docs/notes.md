AI Gateway 
09-09-2026
### Content Learned
Today I learned about AI Gateway and its purpose. An AI Gateway works as a middle layer between the application and AI models. It helps manage requests instead of directly connecting the application to an AI provider. I also learned about provider abstraction and routing. Provider abstraction helps us connect different AI providers using a common structure, while routing decides where the request should be sent.

### Practical Learning
I created a basic AI Gateway using FastAPI. I created a chat API that receives a user message and passes it through the gateway router. I created a common AI provider interface and a Mock Provider to test the gateway without using a real AI model.

### Flow
Client - Chat API - Gateway Router - AI Provider - Response
