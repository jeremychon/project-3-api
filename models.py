import os
from playhouse.db_url import connect
from peewee import *
from flask_login import UserMixin
import datetime

from playhouse.db_url import connect

if os.environ.get('HEROKU_ON'):
    DATABASE = connect(os.environ.get('DATABASE_URL'))
else:
    DATABASE = SqliteDatabase('painpoint.sqlite')


class BaseModel(Model):
    class Meta:
        database = DATABASE

class User(UserMixin, BaseModel):
	full_name = CharField()
	username = CharField()
	email = CharField()
	password = CharField()

class Painpoint(UserMixin, BaseModel):
	owner = ForeignKeyField(User)
	date = DateTimeField(default=datetime.datetime.now)
	head = CharField(max_length=75, default='String10')
	body = TextField()
	attachment = CharField(default='')

class Painpoint_Votes(UserMixin, BaseModel):
	voter = IntegerField()
	post = IntegerField()
	vote = SmallIntegerField()
	date = DateTimeField(default=datetime.datetime.now)

class Category(UserMixin, BaseModel):
	category = CharField()


class Painpoint_Category(UserMixin, BaseModel):
	category = ForeignKeyField(Category)
	painpoint = ForeignKeyField(Painpoint)


class Solution(BaseModel):
	painpoint = ForeignKeyField(Painpoint)
	owner = ForeignKeyField(User)
	date = DateTimeField(default=datetime.datetime.now)
	head = CharField()
	body = TextField()
	attachment = CharField()


class Solution_Votes(BaseModel):
	voter = ForeignKeyField(User)
	post = ForeignKeyField(Painpoint)
	vote = SmallIntegerField()
	date = DateTimeField(default=datetime.datetime.now)



def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Solution, Solution_Votes, Category, Painpoint, Painpoint_Category, Painpoint_Votes], safe = True)
	DATABASE.close()
