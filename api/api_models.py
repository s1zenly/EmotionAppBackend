from pydantic import BaseModel

class Emotion(BaseModel):
    tg_id: int
    emotion_category: str
    emotion_type: str