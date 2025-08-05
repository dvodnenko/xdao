from contextlib import asynccontextmanager

from fastapi import FastAPI

from application.api.user.routes import router as user_router
from infrastructure.database import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    redis_client = get_redis_client()
    create_all_indexes(redis_client)

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router, prefix='/users')
