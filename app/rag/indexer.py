from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
from app.rag.embeddings import get_embeddings
from app.config import settings
import os

def index_faq_documents():
    """Load FAQ documents, chunk them, and store them into pgvector."""
    faq_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "faq")
    
    # Load documents
    loader = DirectoryLoader(faq_dir, glob="**/*.md", loader_cls=TextLoader)
    documents = loader.load()
    
    if not documents:
        print("No FAQ documents found.")
        return

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    
    # Initialize connection to pgvector
    print(f"Indexing {len(chunks)} chunks into PostgreSQL pgvector...")
    vectorstore = PGVector(
        embeddings=get_embeddings(),
        collection_name="faq_collection",
        connection=settings.database_url,
        use_jsonb=True,
    )
    
    # Store documents
    vectorstore.add_documents(chunks)
    print("Indexing complete.")

if __name__ == "__main__":
    index_faq_documents()
