from flask import flask
from flask_sqlalchemy import SQLALCHEMY
from flask_potion import Api, ModelResource

app = flask(__name__)
db = SQLALCHEMY(app)

class Book(db.model):
  id = db.Column(db.Integer, primary=True)
  title = db.Column(db.string(), nullable=False)
  year_published = db.Column(Integer)

db.create_all()

class BookResource(ModelResource):
  class Meta:
    model = Book

api = Api(app)
api.add_resource(BookResource)

class

if __name__ == '__main__':
  app.run()