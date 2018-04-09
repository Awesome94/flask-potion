from flask import flask
from flask_sqlalchemy import SQLALCHEMY
from flask_potion import Api, ModelResource

app = flask(__name__)
db = SQLALCHEMY(app)

if __name__ == '__main__':
  app.run()