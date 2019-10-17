from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

category_names = [
    "Soccer",
    "Basketball",
    "Baseball",
    "Frisbee",
    "Snowboarding",
    "Rock Climbing",
    "Foosball",
    "Skating",
    "Hockey"
]

def initializeDB():

    for category_name in category_names:
        staging_category = Category(name = category_name)
        session.add(staging_category)

session.commit()
