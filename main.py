from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db_config import init_db

@asynccontextmanager
async def lifespan(app_: FastAPI):
    await init_db()
    yield

app = FastAPI(title='Emotion app', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)