#!/usr/bin/pyhton3
"""
Handles the storage when the engine depends on a MySQL database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
    Database based storage system
    """
    __engine = None
    __session = None

    classes = {"User": User, "Place": Place, "State": State, "City": City,
               "Amenity": Amenity, "Review": Review}

    def __init__(self):
        """
        Constructor for DBStorage
        """
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries all object of the same class specified,
        or all object if the class is not specified
        """

        aDict = {}
        objects = []
        if cls:
            objects = self.__session.query(cls)
        else:
            for cls in self.classes.values():
                objects += self.__session.query(cls).all()
        for obj in objects:
            aDict[type(obj).__name__ + '.' + obj.id] = obj
        return aDict

    def new(self, obj):
        """
        Adds the object to the current database session
        """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """
        Commits the changes in the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes objects from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates the current database session from the engine
        """
        Base.metadata.create_all(self.__engine)
        ses_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(ses_factory)
