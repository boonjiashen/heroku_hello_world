import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height_in_cm = Column(Integer)

assert 'DATABASE_URL' in os.environ
engine = create_engine(os.environ['DATABASE_URL'])

Base.metadata.create_all(engine)
