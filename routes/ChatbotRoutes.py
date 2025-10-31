from fastapi import APIRouter
from schames.Chatbot.ChatbotRequest import ChatbotRequest

router = APIRouter()

router.post("")
async def Chatbot(req : ChatbotRequest):
    return print("hello world") 
    
