from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis.commands.search.field import TextField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.exceptions import ResponseError

from application.api.user.routes import router as user_router
from infrastructure.database import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    try:
        create_index(get_redis_client(), 'user_idx', [
            TextField('$.id', as_name='id'),
            TextField('$.name', as_name='name'),
            TextField('$.email', as_name='email'),
        ], definition=IndexDefinition(
            prefix=['user:'], 
            index_type=IndexType.JSON
            ))
    except ResponseError as e:
        print('index already exists')

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router, prefix='/users')
