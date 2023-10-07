from fastapi import APIRouter

router = APIRouter()

@router.get("/v1")
def hello_world():
    return {"message": "Hello, World!"}
