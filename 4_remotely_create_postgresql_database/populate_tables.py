import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_tables import Person, Base
import random

assert 'DATABASE_URL' in os.environ
engine = create_engine(os.environ['DATABASE_URL'])

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

def generate_height():
    "Returns an integer"
    mean_height_in_cm = 180
    stddev_height_in_cm = 15
    return int(random.gauss(mean_height_in_cm, stddev_height_in_cm))

names = """
julie
peter
paul
josh
julia
victoria
vanessa
ali
mak
""".strip().split()

# Menu for UrbanBurger
people = [Person(name=name, height_in_cm=generate_height()) for name in names]

session.add_all(people)
session.commit()

print "added people!"
