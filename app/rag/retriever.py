from langchain_postgres import PGVector
from app.rag.embeddings import get_embeddings
from app.config import settings
from typing import List
from langchain_core.documents import Document

def get_vectorstore() -> PGVector:
    """Return an instance of the PGVector vectorstore."""
    return PGVector(
        embeddings=get_embeddings(),
        collection_name="faq_collection",
        connection=settings.database_url,
        use_jsonb=True,
    )

def retrieve_faq(query: str, k: int = 3) -> str:
    """Search the vector database for relevant FAQ chunks."""
    try:
        vectorstore = get_vectorstore()
        results: List[Document] = vectorstore.similarity_search(query, k=k)
        
        if not results:
            return "No relevant information found in the FAQ database."
            
        combined_text = "\n\n".join([doc.page_content for doc in results])
        return combined_text
    except Exception as e:
        return f"Error retrieving from knowledge base: {str(e)}"
