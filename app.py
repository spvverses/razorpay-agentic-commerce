import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from agent import run_agentic_flow

app = FastAPI(title="Razorpay Agentic Commerce API Engine", version="1.0.0")

class PromptRequest(BaseModel):
    user_query: str

@app.get("/")
def home():
    return {"status": "online", "system": "Razorpay Buildathon Track 1 Core"}

@app.post("/api/v1/agent/commerce")
def execute_commerce_agent(payload: PromptRequest):
    if not payload.user_query.strip():
        raise HTTPException(status_code=400, detail="Query prompt cannot be empty.")
    try:
        result = run_agentic_flow(payload.user_query)
        return {"status": "success", "execution_data": result}
    except Exception as e:
        return {"status": "error", "reason": str(e)}

if __name__ == "__main__":
    # This keeps the server open and running on port 8000
    uvicorn.run("app.py:app", host="127.0.0.1", port=8000, reload=True)
