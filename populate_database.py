from database_setup import Base, Item, Category, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db',
            connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user = User(
    name='Miaan',
    email='miaankatkramer@gmail.com',
)

session.add(user)
session.commit()

category = Category(
    title='Gaming',
)

session.add(category)
session.commit()

item1 = Item(
    name='Headset',
    description='A Razer Chroma 7.1 surround sound headphones',
    category=category,
)

session.add(item1)
session.commit()

print('Database Populated')