import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key = True)

    title = Column(String(80), nullable = False)

class Item(Base):

    __tablename__ = 'category_items'

    id = Column(Integer, primary_key = True)

    cat_id = Column(Integer, ForeignKey('categories.id'), nullable = False)

    name = Column(String(80))

    description = Column(String(250))

    category = relationship(Category)

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)

    name = Column(String(80), nullable = False)

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)