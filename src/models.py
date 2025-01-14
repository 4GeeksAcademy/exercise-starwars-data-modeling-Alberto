import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

    #relationships
    favorites = relationship('Favorites', backref='users')
    
class Favorites(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    diameter = Column(Integer)
    films = Column(ARRAY(String))
    gravity = Column(Integer)
    orbital_period = Column(Integer)
    population = Column(Integer)
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String(250))

    #relationships
    favorites = relationship('Favorites', backref='planets')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    films = Column(ARRAY(String))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(Integer)
    homeworld = Column(String(250))
    mass = Column(Integer)
    skin_color = Column(String(250))
    species = Column(String(250))
    starships = Column(ARRAY(String))
    vehicles = Column(ARRAY(String))

    #relationships
    favorites = relationship('Favorites', backref='characters')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
