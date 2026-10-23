from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI(title="Authentication Microservice", version="1.0.0")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_seconds: int = 3600

@app.get("/api/v1/auth/health")
def health():
    return {"status": "auth-service-ready"}
