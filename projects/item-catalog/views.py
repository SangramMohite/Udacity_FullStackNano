
from models import Base, User, Category, Item
from flask import Flask, jsonify,request, url_for, abort, g, render_template, redirect
from flask_httpauth import HTTPBasicAuth
from flask import make_response


import httplib2
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
from models import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session=DBSession()

app = Flask(__name__)

@app.route('/')
@app.route('/categories/')
def index():
	categories = session.query(Category).all()
	return render_template('index.html', categories=categories)

@app.route('/categories/<int:category_id>/', methods=['GET'])
@app.route('/categories/<int:category_id>/items/', methods=['GET'])
def items_in_category(category_id):
	children = session.query(Category).filter_by(parent_id=category_id).all()
	if (children):
		return render_template('items.html', categories=children)
	else:
		return jsonify({'data': 'leaf Nodes'})

@app.route('/categories/new/', methods=['POST', 'GET'])
def add_new_category():
	categories = session.query(Category).all()
	if (request.method == 'POST'):
		name = request.form['name']
		description = request.form['description']
		parent_category = request.form['parent']

		if (name):
			if (parent_category):
				for category in categories:
					if (parent_category == category.category_name):
						parent = category.id
			else:
				parent = None

			
				new_category = Category(
					category_name = name,
					description = description,
					parent_id=parent, 
					user_id='1')
				session.add(new_category)
				session.commit()
				return redirect(url_for('index'))
		else:
			return render_template('newcategory.html', categories=categories)
	else:
			return render_template('newcategory.html', categories=categories)

@app.route('/categories/<int:category_id>/edit/', methods=['GET','POST'])
def edit_category(category_id):
	category_to_edit = session.query(Category).filter_by(id=category_id).one()
	all_categories = session.query(Category).all()

	if (category_to_edit.parent_id):
		for category in all_categories:
			if category_to_edit.parent_id == category.id:
				parent_name = category.category_name
				break
	else:
		parent_name = None

	if (category_to_edit):
		if (request.method == 'POST'):
			name = request.form['name']
			description = request.form['description']
			parent_category = request.form['parent']

			category_to_edit.category_name = name
			category_to_edit.description = description
			category_to_edit.parent_id=parent 
			session.commit()
			return redirect(url_for('index'))
		else:
			return render_template('editcategory.html', category=category_to_edit, parent=parent_name, categories=all_categories)
	else:
		return render_template('editcategory.html', category=category_to_edit, parent=parent_name,categories=all_categories)

@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def delete_category(category_id):
	category_to_delete = session.query(Category).filter_by(id=category_id).one()
	if (category_to_delete):
		if (request.method == 'POST'):
			print "In POST delete"
			session.delete(category_to_delete)
			session.commit()
			return redirect(url_for('index'))
		else:
			return render_template('deletecategory.html', category=category_to_delete)
	else:
		return render_template('deletecategory.html', category=category_to_delete)

@app.route('/categories/<int:category_id>/items/new/', methods=['GET', 'POST'])
def new_item(category_id):
	return jsonify({'data': 'Add an item to category'})

@app.route('/categories/<int:category_id>/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def edit_item(category_id, item_id):
	return jsonify({'data': 'Edit an item'})

@app.route('/categories/<int:category_id>/items/<int:item_id>/delete/', methods=['GET', 'POST'])
def delete_item(category_id, item_id):
	return jsonify({'data': 'Delete an item'})



if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
