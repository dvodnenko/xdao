from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from domain.user.services import UserService
from infrastructure.database.dao.user_dao import SQLAlchemyUserDAO
from db import get_sql_session


router = APIRouter()


def get_user_service(session: Session = Depends(get_sql_session)) -> UserService:
    dao = SQLAlchemyUserDAO(session)
    return UserService(dao)

@router.post('/register')
def register(name: str, email: str, service: UserService = Depends(get_user_service)):
    return service.register_user(name, email)
