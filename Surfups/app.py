import numpy as np
import pandas as pd 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

Base.prepare(engine, reflect=True)
print(Base.classes.keys())

# Save reference to the table
Measurement= Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

# last 12 months variable
last_twelve_months = '2016-08-23'

#most active station variable
active_station_id= 'USC00519281'

# Flask Routes "List all available api routes.
@app.route("/")
def welcome():
    
    return (f"Welcome to Climate API!"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
   
    prcp_scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_twelve_months).all()
    session.close()
    prcp_list = list(np.ravel(prcp_scores))
    return jsonify(prcp_list)
 
# Create our session (link) from Python to the DB and create a route and  jsonify the station list

@app.route("/api/v1.0/stations")   
def stations():
    session = Session(engine)
    stations= session.query(Station.station,Station.name).all()
    session.close()
    station_list = list(np.ravel(stations))
    return jsonify(station_list)

# Create our session (link) from Python to the DB and create a route and  jsonify the temperature observation list

@app.route("/api/v1.0/tobs")     

def tobs():
    session = Session(engine)
    tobs= session.query(Measurement.date,Measurement.tobs).filter(Measurement.station == active_station_id).filter(Measurement.date >= last_twelve_months).all()
    session.close()
    tobs_list = list(np.ravel(tobs))
    return jsonify(tobs_list)
# Create our session (link) from Python to the DB and create a route to get the tmin,tavg,tmax that greater than or equal to the start date
#  and  jsonify the start date list
@app.route("/api/v1.0/<start>") 
def tempstart(start):
    format_date = dt.datetime.strptime(start, '%d-%m-%Y').date()
    session = Session(engine)
    start_query = session.query(Measurement.station, func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date>= format_date).all()
    session.close()
    start_list = list(np.ravel(start_query))
    return jsonify(start_list)
    
# Create our session (link) from Python to the DB and create a route to get the tmin,tavg,tmax 
# that for the dates from the start date to the end date

@app.route("/api/v1.0/<start>/<end>") 
def tempstartend(start,end):
    format_start = dt.datetime.strptime(start, '%d-%m-%Y').date()
    format_end = dt.datetime.strptime(end, '%d-%m-%Y').date()
    session = Session(engine)
    start_end_query = session.query(Measurement.station, func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date>= format_start).filter(Measurement.date <= format_end).all()
    session.close()
    start_end_list = list(np.ravel(start_end_query))
    return jsonify(start_end_list)
if __name__ == "__main__":
    app.run(debug=True)













