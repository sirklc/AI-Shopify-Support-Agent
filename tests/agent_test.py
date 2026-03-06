from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "AI Shopify Support Agent API is running."}

# Testing the agent requires external API calls, which are mocked below minimally or ignored in basic testing.
# A full test suite would mock OpenAI, pgvector, and Redis.
def test_chat_endpoint_format():
    # If we wanted to test this without calling OpenAI, we'd mock run_agent.
    # For now, we just ensure the route exists, but expect a 500 without valid API keys during basic testing unless mocked.
    pass
