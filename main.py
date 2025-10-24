from fastapi import FastAPI, Request
from pydantic import BaseModel
from middleware import APIFirewallMiddleware

app = FastAPI(title="API Firewall - Advanced Protection")

# Add API Firewall Middleware
app.add_middleware(APIFirewallMiddleware)

# Pydantic model for test endpoint
class TestRequest(BaseModel):
    message: str

@app.post("/test")
async def test_endpoint(data: TestRequest):
    return {"received_message": data.message}

@app.get("/")
async def home():
    return {"message": "API Firewall is active and monitoring traffic."}
