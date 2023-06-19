#!/usr/bin/python3

from sqlalchemy import Column,Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

username = 'root'
password = 'Muriithi.1991'
database_name ='hbtn_0e_6_usa'
connection_url = f'mysql://{username}:{password}@localhost:3306/{database_name}'

engine = create_engine(connection_url)

Base.metadata.create_all(engine)
