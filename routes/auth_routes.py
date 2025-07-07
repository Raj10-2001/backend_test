from fastapi import APIRouter, HTTPException
from models.schemas import LoginRequest
from services.auth_service import authenticate_user

router = APIRouter()

@router.post("/login/")
def login(request: LoginRequest):
    token = authenticate_user(request.username, request.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"token": token}
