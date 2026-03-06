from app.tools.shopify_tool import get_order
from app.tools.shipment_tool import track_shipment
from app.tools.faq_tool import faq_search
from app.tools.refund_tool import refund_request

# List of all tools available to the agent
support_tools = [get_order, track_shipment, faq_search, refund_request]
