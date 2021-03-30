#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import City
from os import getenv


class State(BaseModel, Base):
    """
    Class States
    """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        from models import storage

        @property
        def cities(self):
            st_cities = []
            for city in storage.all(City):
                if (self.id == city.state_id):
                    st_cities.append(city)
            return st_cities
