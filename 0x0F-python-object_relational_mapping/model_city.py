#!/usr/bin/python3
"""Python file similar to model_state.py"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """inherits from Base (imported from model_state)
    links to the MySQL table cities
    class attribute id
    class attribute name
    class attribute state_id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
