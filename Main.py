from fastapi import FastAPI
from routes.ChatbotRoutes import router as chatbot_router

app = FastAPI(
    title="Hybrid Chatbot API",
    description="Chatbot dengan TF-IDF + Semantic Embedding + Gemini",
    version="1.0.0"
)

# Daftarkan router
app.include_router(chatbot_router)




