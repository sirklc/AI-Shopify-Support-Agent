from langchain_community.chat_message_histories import RedisChatMessageHistory
from app.config import settings

def get_message_history(session_id: str) -> RedisChatMessageHistory:
    """Retrieve or create a chat message history for a given session ID in Redis."""
    return RedisChatMessageHistory(
        session_id=session_id,
        url=settings.redis_url
    )
