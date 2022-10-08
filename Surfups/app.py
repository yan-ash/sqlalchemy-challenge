import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement= Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

# last 12 months variable
last_twelve_months = '2016-08-23'

#most active station variable
active_station_id= 'USC00519281'

# Flask Routes "List all available api routes.
@app.route("/")
def welcome():
    
    return (f"Welcome to my API!"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
   
    prcp_scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_twelve_months).all()
    session.close()
    return jsonify(prcp_scores)


@app.route("/api/v1.0/stations")   
def stations():
    session = Session(engine)
    stations= session.query(Station.station,Station.name).all()
    session.close()
    return jsonify(stations)

@app.route("/api/v1.0/tobs")     

def stations():
    session = Session(engine)
    stations= session.query(Measurement.date,Station.tobs).filter(Measurement.station == active_station_id).filter(Measurement.date >= last_twelve_months).all()
    session.close()
    return jsonify(stations)










