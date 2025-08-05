from uuid import UUID

from fastapi import APIRouter, Depends
from redis import Redis

from domain import *
from infrastructure.database import *
from infrastructure.schemas import UserSchema


router = APIRouter()


def get_user_service(redis: Redis = Depends(get_redis_client)) -> UserService:
    dao = RedisUserDAO(redis)
    return UserService(dao)

@router.post('/register')
def register(user: UserSchema, service: UserService = Depends(get_user_service)):
    return service.register_user(user)

@router.get('/get_by_id')
def get_by_id(id: UUID, service: UserService = Depends(get_user_service)):
    return service.get_profile(id)
