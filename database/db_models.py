from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import BigInteger, DateTime, ForeignKey

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


class EmotionHistory(Base):
    __tablename__ = 'emotion_history'

    id: Mapped[int] = mapped_column(primary_key=True)
    emotion_category: Mapped[str] = mapped_column(nullable=False)
    emotion_type: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))