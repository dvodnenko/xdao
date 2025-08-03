from uuid import UUID

from fastapi import APIRouter, Depends
from redis import Redis

from domain import *
from infrastructure.database import *


router = APIRouter()


def get_user_service(redis: Redis = Depends(get_redis_client)) -> UserService:
    dao = RedisUserDAO(redis)
    return UserService(dao)

@router.post('/register')
def register(name: str, email: str, service: UserService = Depends(get_user_service)):
    return service.register_user(name, email)

@router.get('/get_by_id')
def get_by_id(id: UUID, service: UserService = Depends(get_user_service)):
    return service.get_profile(id)
