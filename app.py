from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def login():
    return "Login Page"

@app.route('/register')
def register():
    return "Register Page"

# Categories
@app.route('/categories')
def listCategory():
    return "List Categories"

@app.route('/categories/<int:cat_id>/')
def showCategory():
    return "Show Category"

@app.route('/categories/<int:cat_id>/edit')
def editCategory():
    return "Edit Category"

@app.route('/categories/<int:cat_id>/delete')
def deleteCategory():
    return "Delete Category"

@app.route('/categories/<int:cat_id>/items')
def listCategoryItems(cat_id):
    category = session.query(Category).filter_by(id = cat_id).one()
    items = session.query(Item).filter_by(cat_id = category.id)
    return render_template('templates/categories_show.html', category=category, items=items)

if __name__ == '__main__':
    app_secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
