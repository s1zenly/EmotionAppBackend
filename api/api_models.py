from pydantic import BaseModel, ConfigDict

from typing import List

class Emotion(BaseModel):
    tg_id: int
    emotion_category: str
    emotion_types: List[str]

    model_config = ConfigDict(from_attributes=True)

class Quote(BaseModel):
    quote_text: str
    quote_author: str

    model_config = ConfigDict(from_attributes=True)