from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from redis import Redis

from domain.user.services import UserService
from infrastructure.database.dao.user_dao import RedisUserDAO
from db import get_redis


router = APIRouter()


def get_user_service(redis: Redis = Depends(get_redis)) -> UserService:
    dao = RedisUserDAO(redis)
    return UserService(dao)

@router.post('/register')
def register(name: str, email: str, service: UserService = Depends(get_user_service)):
    return service.register_user(name, email)

@router.get('/get_by_id')
def get_by_id(id: UUID, service: UserService = Depends(get_user_service)):
    return service.get_profile(id)
