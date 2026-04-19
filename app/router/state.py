from fastapi import APIRouter
from app.persistence import save_state, load_state

router = APIRouter()

@router.get("/state/{key}")
def get_state(key: str):
    return {"key": key, "value": load_state(key)}

@router.post("/state/{key}")
def set_state(key: str, value: str):
    save_state(key, value)
    return {"key": key, "status": "saved"}
