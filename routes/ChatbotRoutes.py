from fastapi import APIRouter
from fastapi import APIRouter, HTTPException
from schames.Chatbot.ChatbotRequest import ChatbotRequest
from schames.Chatbot.ChatbotRespond import ChatbotRespond
from service.ChatbotService import get_chatbot_response

router = APIRouter(prefix="/api")

@router.post("/", response_model=ChatbotRespond)
async def chatbot(req: ChatbotRequest):
    try:
        answer = get_chatbot_response(req.query)
        return ChatbotRespond(question=req.query,answer=answer) 
    except FileNotFoundError: 
        raise HTTPException(status_code=404, detail="Data Tidak di temukan")
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
    
