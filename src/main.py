from fastapi import FastAPI
from app.user.routes import router as user_router
from infrastructure.database.models.user_model import Base
from db import engine


app = FastAPI()

app.include_router(user_router, prefix='/users')


Base.metadata.create_all(bind=engine)
