from pydantic import BaseModel

class ChatbotRespond(BaseModel):
    question : str
    answer : str

        