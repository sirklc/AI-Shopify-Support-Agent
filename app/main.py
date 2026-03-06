from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import routes
from app.rag.indexer import index_faq_documents
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run indexer in background on startup to populate pgvector
    asyncio.create_task(asyncio.to_thread(index_faq_documents))
    yield

app = FastAPI(
    title="AI Shopify Support Agent",
    description="Autonomous AI support agent for Shopify stores.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "AI Shopify Support Agent API is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
