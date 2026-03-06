from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.agents.support_agent import run_agent
from app.memory.redis_memory import get_message_history

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    response: str
    session_id: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    # Retrieve chat history
    history = get_message_history(request.session_id)
    
    # Run the agent
    agent_response = run_agent(request.message, history.messages)
    
    # Save the interaction to memory
    history.add_user_message(request.message)
    history.add_ai_message(agent_response)
    
    return ChatResponse(
        response=agent_response,
        session_id=request.session_id
    )
