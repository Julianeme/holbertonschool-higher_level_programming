#!/usr/bin/python3
""""
contains the class definition of a State and an instance Base=declarative_base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base

Base = declarative_base()


class City(Base):
    """City database"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
