from sqlalchemy import select, delete, func, insert


from database.db_models import User, EmotionHistory, EmotionType
from database.db_config import async_session

from datetime import datetime

import hashlib
import json


async def add_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:
            return user
        
        new_user = User(tg_id=tg_id)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user
    
async def add_emotion(_user_id, _emotion_category, _emotion_types):
    async with async_session() as session:
        _create_date = datetime.now()
        _emotion_types_hash = create_unique_hash(_user_id, _emotion_category, _create_date)

        emotion_history = EmotionHistory(
            emotion_category=_emotion_category,
            emotion_types_key=_emotion_types_hash,
            create_date=_create_date,
            user_id=_user_id
        )

        emotion_types = [dict(uuid=_emotion_types_hash, emotion_type=current_emotion) for current_emotion in _emotion_types]

        session.add(emotion_history)

        await session.execute(insert(EmotionType.__table__).values(emotion_types))

        await session.commit()


def create_unique_hash(*args):
    args_str = [str(arg) for arg in args]
    data = json.dumps(args_str, sort_keys=True)
    return hashlib.sha256(data.encode()).hexdigest()