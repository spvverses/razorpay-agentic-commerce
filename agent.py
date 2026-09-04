import json

MOCK_INVENTORY = [
    {"id": "prod_1", "name": "Premium Leather Wallet", "price": 1500, "stock": 5},
    {"id": "prod_2", "name": "Minimalist Card Holder", "price": 800, "stock": 12}
]

def run_agentic_flow(user_prompt: str) -> dict:
    """Simulates basic structured processing matching the interface expectations."""
    return {
        "input": user_prompt,
        "audit_trail": [
            {"action": "Checked Local Inventory Store", "result": MOCK_INVENTORY}
        ],
        "response": {
            "status": "payment_contract_ready",
            "product_name": "Premium Leather Wallet",
            "amount_inr": 1500
        }
    }
