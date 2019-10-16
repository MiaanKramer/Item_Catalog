import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

Base = declarative_base()

class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)

    title = Column(String(80), nullable = False)

class Item(Base):

    __tablename__ = 'item'

    id = Column(Integer, primary_key = True)

    cat_id = Column(Integer, ForeignKey('category.id'), nullable = False)

    name = Column(String(80))

    description = Column(String(250))

    category = relationship(Category)

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)

    name = Column(String(80))

engine = create_engine(
    'sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)