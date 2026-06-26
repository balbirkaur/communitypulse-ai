"""Chat API endpoints."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.agents.decision_engine import decision_engine

router = APIRouter(prefix="/api/chat", tags=["chat"])


class ChatMessage(BaseModel):
    """Chat message model."""
    content: str
    context: Optional[dict] = None


class ChatResponse(BaseModel):
    """Chat response model."""
    response: str
    metadata: Optional[dict] = None


@router.post("/message", response_model=ChatResponse)
async def send_message(message: ChatMessage):
    """Send a message to the AI decision engine."""
    try:
        # Process through decision engine
        result = await decision_engine.process_query(
            message.content,
            message.context
        )
        
        return ChatResponse(
            response=str(result),
            metadata={"engine": "decision_engine", "status": result.get("status")}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history")
async def get_chat_history(limit: int = 10):
    """Get chat history."""
    try:
        return {
            "status": "success",
            "messages": [],
            "limit": limit
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
