# mem0/server/routes/memory_dashboard.py

from fastapi import APIRouter
from mem0 import Memory

router = APIRouter()
memory = Memory()

@router.get("/users/{user_id}/memories")
def list_user_memories(user_id: str):
    return memory.list(user_id=user_id)

@router.delete("/users/{user_id}/memories/{memory_id}")
def delete_user_memory(user_id: str, memory_id: str):
    memory.delete(memory_id, user_id=user_id)
    return {"status": "deleted"}
