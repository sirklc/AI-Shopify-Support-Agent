from pydantic import BaseModel, Field
from langchain_core.tools import tool

class RefundRequestInput(BaseModel):
    order_id: str = Field(description="The unique identifier for the order to be refunded.")

@tool("refund_request", args_schema=RefundRequestInput)
def refund_request(order_id: str) -> str:
    """Initiate a refund request for a specific order."""
    # Mock Refund functionality
    valid_orders = ["#123", "123", "#555", "555"]
    
    if order_id not in valid_orders:
        return f"Cannot process refund: Order {order_id} not found."
        
    return f"Refund request for order {order_id} has been successfully initiated. Funds will be returned to the original payment method within 3-5 business days."
