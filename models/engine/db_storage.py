#!/usr/bin/python3
""" New engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.base_model import BaseModel


class DBStorage:
    """ The engine linked to the MySQL """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of the DBstorage"""

        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if os.gentenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=engine)

    def all(self, cls=None):
        """ Query on the current database session all objects """
        pass

    def new(self, obj):
        """ add the object to the current database session """
        pass

    def save(self):
        """ commit all changes of the current database session """
        pass

    def reload(self):
        """ create all tables in the database"""
        pass
