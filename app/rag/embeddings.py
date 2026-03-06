from langchain_openai import OpenAIEmbeddings
from app.config import settings

def get_embeddings() -> OpenAIEmbeddings:
    """Initialize and return the OpenAI embeddings model."""
    return OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=settings.openai_api_key
    )
