from fastapi import APIRouter, WebSocket
from pydantic import BaseModel

chat_router = APIRouter(prefix="/chat")


class ChatRequest(BaseModel):
    """Request model for chat messages."""

    persona: str
    message: str


class ChatResponse(BaseModel):
    """Response model for chat messages."""

    persona: str
    message: str


@chat_router.post("")
async def chat(request: ChatRequest) -> ChatResponse:
    """Send a chat message and wait for a response."""
    return ChatResponse(persona=request.persona, message=f"Echo! {request.message}")


@chat_router.websocket(".stream")
async def open_chat_stream(ws: WebSocket) -> None:
    """Open a chat stream."""
    await ws.accept()
    try:
        while True:
            data = await ws.receive_text()
            await ws.send_text(f"Echo! {data}")
    finally:
        await ws.close()
