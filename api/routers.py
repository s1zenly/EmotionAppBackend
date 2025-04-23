from main import app
from api_models import Emotion
import database.db_client as db_client

@app.post("/api/emotion/add")
async def save_emotion(emotion: Emotion):
    user = await db_client.add_user(emotion.tg_id)
    await db_client.add_emotion(user.id, emotion.emotion_category, emotion.emotion_type)

    return {'status': 'ok'}