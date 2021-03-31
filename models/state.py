#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """
    Class States
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
              cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:

        @property
        def cities(self):
            """
            Getter for cities related to a state using a FIlEStorage engine
            """
            st_cities = []
            for city in storage.all(City):
                if (self.id == city.state_id):
                    st_cities.append(city)
            return st_cities
