from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api_models import Emotion
import database.db_client as db_client

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

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

@app.post("/api/emotion/add")
async def save_emotion(emotion: Emotion):
    user = await db_client.add_user(emotion.tg_id)
    await db_client.add_emotion(user.id, emotion.emotion_category, emotion.emotion_types)

    return {'status': 'ok'}