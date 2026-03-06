from pydantic import BaseModel, Field
from langchain_core.tools import tool
from typing import Dict

class TrackShipmentInput(BaseModel):
    order_id: str = Field(description="The unique identifier for the order system to track shipping.")

@tool("track_shipment", args_schema=TrackShipmentInput)
def track_shipment(order_id: str) -> str:
    """Check the current shipping status of an order."""
    # Mock Shipment API response
    mock_db = {
        "#123": "Your order is currently being processed and will ship soon.",
        "#555": "Your order was shipped yesterday via DHL. Tracking number: DHL123456789.",
        "123": "Your order is currently being processed and will ship soon.",
        "555": "Your order was shipped yesterday via DHL. Tracking number: DHL123456789."
    }
    
    status = mock_db.get(order_id)
    if not status:
        return f"Could not find shipping information for order {order_id}."
    
    return status
