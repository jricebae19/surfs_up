#Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#Import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Import flask dependency and jsonify
from flask import Flask, jsonify

#Create the engine
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflect database into classes
Base = automap_base()

#Reflect database
Base.prepare(engine, reflect=True)

#Creating variable for each class
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create session link from Python to the database
session = Session(engine)

#Define flask app
app = Flask(__name__)

#Add welcome statement
def welcome():
    return(
     '''   
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api.v1.0/stations
    /api.v1.0/tobs
    /api.v1.0/temp/start/end
    ''')