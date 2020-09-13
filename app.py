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
@app.route("/")
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

#Add precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#Add stations route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)