from pydantic import BaseModel

from typing import List

class Emotion(BaseModel):
    tg_id: int
    emotion_category: str
    emotion_types: List[str]