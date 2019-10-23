from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Class to create the categories table
class Category(Base):

    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)

    title = Column(String(250), nullable = False)

    # return object serialized
    @property
    def serialize(self):

        return {
            'id': self.id,
            'title': self.title,
        }

# Class to create the items table
class Item(Base):

    __tablename__ = "category_items"

    id = Column(Integer, primary_key = True)

    cat_id = Column(Integer, ForeignKey('categories.id'), nullable = False)

    name = Column(String(250))

    description = Column(String(250))

    category = relationship(Category)

    # return object serialized
    @property
    def serialize(self):

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'cat_id': self.cat_id
        }

# Class to create the users table
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable = False)

    email = Column(String(250))

    # return object serialized
    @property
    def serialize(self):

        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)