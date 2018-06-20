import os
import sys
from sqlalchemy import Column, ForeignKey,Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as pwd_context
import random, string
from sqlalchemy import create_engine

from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, 
	BadSignature, SignatureExpired)

Base = declarative_base()
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits)
	for x in xrange(32))

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True, autoincrement='ignore_fk')	
	username = Column(String(32), index = True)
	picture = Column(String)
	email = Column(String)
	passowrd_hash = Column(String(64))

	def hash_passowrd(self, password):
		self.passowrd_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(passowrd, self.passowrd_hash)

	def generate_auth_token(self, expiration=600):
		s = Serializer(secret_key, expires_in=expiration)
		return s.dumps({'id':self.id})

	@staticmethod
	def verify_auth_token(token):
		s = Serializer(secret_key)
		try:
			data  = s.loads(token)
		except SignatureExpired:
			# valid token but expired
			return None
		except BadSignature:
			# invalid token
			return None
		user_id = data['id']
		return user_id

	@property
	def serialize(self):
		return {
			'username': self.username,
			'email':	self.email,
			'picture':	self.picture
		}


class Category(Base):
	__tablename__ = 'category'
	id = Column(Integer, primary_key=True, autoincrement='ignore_fk')
	category_name = Column(String(64), nullable=False)
	description = Column(String)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)
	parent_id = Column(Integer, ForeignKey('category.id'))
	children = relationship("Category")

	@property
	def serialize(self):
		return {
			'category': self.category_name,
			'description': self.description
		}


class Item(Base):
	__tablename__ = 'item'
	id = Column(Integer, primary_key=True, autoincrement='ignore_fk')
	item_name = Column(String(64), index = True, nullable = False)
	picture = Column(String)
	description = Column(String)
	price = Column(String)
	category_id = Column(String, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'name': self.item_name,
			'description': self.description,
			'picture':	slef.picture,
			'category': self.category_id
		}

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)