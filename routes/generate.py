from fastapi import APIRouter
from models.request_model import PromptRequest
from services.llm_service import generate_code

router = APIRouter()

@router.post("/generate")
def generate(request: PromptRequest):
    result = generate_code(request.prompt)
    return {"output": result}