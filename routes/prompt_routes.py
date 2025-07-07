from fastapi import APIRouter, HTTPException, Header
from models.schemas import PromptRequest
from services.auth_service import get_username_from_token, add_prompt, get_user_history

router = APIRouter()

@router.post("/prompt/")
def submit_prompt(request: PromptRequest, Authorization: str = Header(None)):
    if not Authorization or not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    token = Authorization.split(" ")[1]
    username = get_username_from_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    response = add_prompt(username, request.prompt)
    return {"response": response}

@router.get("/history/")
def get_history(Authorization: str = Header(None)):
    if not Authorization or not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    token = Authorization.split(" ")[1]
    username = get_username_from_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    return get_user_history(username)
