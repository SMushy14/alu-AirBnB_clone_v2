#!/usr/bin/python3
""" State Module for HBNB project """
import models
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",cascade="all, delete-orphan")
    
    if STORAGE_TYPE != 'db':
        name = ''
        cities = []
        @property
        def cities(self):
            """Returns the cities in this State"""
            city_list = []
            for city in models.storage.all(City):
                if citystate_id == self.id:
                    city_list.append(city)
            return city_list        
