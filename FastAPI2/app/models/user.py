from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app.models import *


class Person(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    grade = Column(Integer)
    age = Column(Integer)
    tasks = relationship('Task', back_populates='user')


print(CreateTable(Person.__table__))