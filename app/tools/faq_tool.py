from pydantic import BaseModel, Field
from langchain_core.tools import tool
from app.rag.retriever import retrieve_faq

class FAQSearchInput(BaseModel):
    question: str = Field(description="The customer's question regarding policies, shipping, or general information.")

@tool("faq_search", args_schema=FAQSearchInput)
def faq_search(question: str) -> str:
    """Search the internal knowledge base for answers to common questions."""
    return retrieve_faq(question)
