import os
from flask import Flask
from setup_tables import Person, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Boiler-plate stuff
assert 'DATABASE_URL' in os.environ
engine = create_engine(os.environ['DATABASE_URL'])
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
def hello():
    return " Woohoo! Hello world!"

@app.route("/people")
def show_people():
    people = session.query(Person).all()
    return '<p>'.join([person.name + " " + str(person.height_in_cm)
        for person in people])
