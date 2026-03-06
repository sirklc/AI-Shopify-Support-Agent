from pydantic import BaseModel, Field
from langchain_core.tools import tool
from typing import Dict, Any

class GetOrderInput(BaseModel):
    order_id: str = Field(description="The unique identifier for the order, usually starting with # or a number.")

@tool("get_order", args_schema=GetOrderInput)
def get_order(order_id: str) -> Dict[str, Any]:
    """Retrieve details for a specific Shopify order by its ID."""
    # Mock Shopify API response
    mock_db = {
        "#123": {"status": "paid", "items": ["Blue T-Shirt", "Jeans"], "total": 89.99, "customer": "John Doe"},
        "#555": {"status": "fulfilled", "items": ["Sneakers"], "total": 120.00, "customer": "Jane Smith"},
        "123": {"status": "paid", "items": ["Blue T-Shirt", "Jeans"], "total": 89.99, "customer": "John Doe"},
        "555": {"status": "fulfilled", "items": ["Sneakers"], "total": 120.00, "customer": "Jane Smith"}
    }
    
    order = mock_db.get(order_id)
    if not order:
        return {"error": f"Order {order_id} not found."}
    
    return order
