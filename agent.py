import json

# The store database inventory
MOCK_INVENTORY = [
    {"id": "prod_1", "name": "Premium Leather Wallet", "price": 1500, "stock": 5},
    {"id": "prod_2", "name": "Minimalist Card Holder", "price": 800, "stock": 12}
]

def run_agentic_flow(user_prompt: str) -> dict:
    """Processes user queries and applies strict fintech math logic."""
    # Step 1: Default baseline setup
    product = MOCK_INVENTORY[0] # Default to the wallet
    price_per_item = product["price"]
    quantity = 1 # Default count
    
    # Step 2: Read the number typed by the user in the prompt text
    # A simple string search checks if the user typed common digits
    for count in ["50", "20", "10", "5", "4", "3", "2"]:
        if count in user_prompt:
            quantity = int(count)
            break
            
    total_amount = price_per_item * quantity
    audit_logs = [{"action": "Checked Local Inventory Store", "result": MOCK_INVENTORY}]

    # Step 3: Enforce strict boundaries (The Razorpay Bar)
    # Scenario A: Check stock limits
    if quantity > product["stock"]:
        error_msg = f"Requested quantity ({quantity}) exceeds available inventory stock ({product['stock']})."
        audit_logs.append({"action": "Inventory Gate Check Failed", "reason": error_msg})
        return {
            "input": user_prompt,
            "audit_trail": audit_logs,
            "response": {"status": "error_out_of_stock", "message": error_msg}
        }

    # Scenario B: Check hard spending cap limits
    if total_amount > 10000:
        error_msg = f"Transaction total (INR {total_amount}) exceeds maximum agent spend limit (Max 10,000 INR)."
        audit_logs.append({"action": "Financial Guardrail Gate Blocked", "reason": error_msg})
        return {
            "input": user_prompt,
            "audit_trail": audit_logs,
            "response": {"status": "error_spend_limit_exceeded", "message": error_msg}
        }

    # Scenario C: Everything passes safely
    audit_logs.append({"action": "Financial Verification Passed", "total_calculated": total_amount})
    return {
        "input": user_prompt,
        "audit_trail": audit_logs,
        "response": {
            "status": "payment_contract_ready",
            "product_name": product["name"],
            "quantity": quantity,
            "amount_inr": total_amount,
            "requires_user_pin": True
        }
    }
