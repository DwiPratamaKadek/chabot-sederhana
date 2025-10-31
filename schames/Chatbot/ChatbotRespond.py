from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    id : str
    question : str
    answer : str

        