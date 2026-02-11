from sqlalchemy import Column, SmallInteger, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db import Base

class WorldVote(Base):
    __tablename__ = "world_votes"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    world_id = Column(UUID(as_uuid=True), ForeignKey("worlds.id", ondelete="CASCADE"), primary_key=True)

    vote = Column(SmallInteger)  # -1 or 1
