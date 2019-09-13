# coding=utf-8

from datetime                       import datetime
from sqlalchemy                     import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative     import declarative_base
from sqlalchemy.orm                 import sessionmaker

# Configuration
dbURL   = 'localhost:5432'
dbName  = 'plugins'
dbUser  = 'postgres'
dbPass  = 'stef4o123'
engine  = create_engine(f'postgresql://{dbUser}:{dbPass}@{dbURL}/{dbName}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


# Entity Object

class Entity():
    id                  = Column(Integer, primary_key=True)
    created_at          = Column(DateTime)
    updated_at          = Column(DateTime)
    last_updated_by     = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
    