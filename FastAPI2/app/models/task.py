from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app.models import *


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    text_url = Column(String)
    video_url = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True)
    user = relationship('Person', back_populates='tasks')


print(CreateTable(Task.__table__))

