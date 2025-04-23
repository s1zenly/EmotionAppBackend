from pydantic import BaseModel, ConfigDict

class EmotionSchema(BaseModel):
    id: int
    emotion_category: str
    emotion_type: str
    create_date: str

    model_config = ConfigDict(from_attributes=True)
