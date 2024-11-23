import json
from fastapi import APIRouter
from app.schemas import UserCreateSchema
from app.producer import produce


router = APIRouter()


@router.post("/create")
async def create_user(data: UserCreateSchema) -> dict:
    data_string = json.dumps(data.model_dump())
    await produce("test_queue", data_string.encode())

    return {"msg": "Message successfully sended !"}
