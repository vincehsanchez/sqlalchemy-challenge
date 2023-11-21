# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pandas as pd
import datetime as dt
#could it not have been working because i had more than one end?
from matplotlib import style ##
style.use('fivethirtyeight') ##
import matplotlib.pyplot as plt ##
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite") #do i need to desigate folder?
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save references to the table
print(Base.classes.keys())
measurement_ref = Base.classes.measurement
station_ref = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
#################################################
# Flask Setup
##################################################
# 1. import Flask
from flask import Flask, jsonify
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)
# 3. Define what to do when a user hits the index route #why does this work only from another file?
@app.route("/")
def congrats():
    #print("Server received request for 'welcome' page...")
    return (
        f"Congratulations!<br/>"
        f"You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii.<br/>"
        f"To help with your trip planning, here is a climate analysis about the area.<br/>" 
        f"The following sections will help accomplish this!<br/>"
        f"<br/>"
        f"Things to consider (Routes) to help you plan:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"
    )
# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    #print("Server received request for 'precipitation' page...")
    last_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Perform a query to retrieve the data and precipitation scores
    #we have date range, find precipitation
    precipitty_data = session.query(measurement_ref.date, measurement_ref.prcp).\
        filter(measurement_ref.date >= last_year_date).all()
    session.close()
        #we need dict
    all_precipitty = []
    for date, prcp in precipitty_data:
        precipitty_dict = {}
        precipitty_dict["date"] = date
        precipitty_dict["prcp"] = prcp
        all_precipitty.append(precipitty_dict)
    '''Precipitation of Past Year'''
    return jsonify(all_precipitty)
        
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    # Query all stations
    all_stations = session.query(station_ref.station).all()
    session.close()
    station_list = list(np.ravel(all_stations))
    '''Look at all these stations'''
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    last_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temp_data = session.query(measurement_ref.tobs).\
    filter(measurement_ref.station == 'USC00519281').\
    filter(measurement_ref.date >= last_year_date).all()
    session.close()
    temps_list = list(np.ravel(temp_data))
    return jsonify(temps_list)

@app.route("/api/v1.0/<start>") # ithink this is from any start to the end of date range..
def user_start(start_date):
    session = Session(engine)
    temp_data = session.query(measurement_ref.tobs)
    """Fetch the max, min, avg of temps with start_date that is within
       the date range, or a 404 if not."""
    select_date_temps = [func.min(measurement_ref.tobs), func.max(measurement_ref.tobs), func.avg(measurement_ref.tobs)] #use 'avg' not 'mean'
    if not end:
        date_query == session.query(*sel) #TA James and Zeb suggested to go this route.
    return jsonify(date_query)
    #canonicalized = start_date.replace(" "," ").lower()
    #for character in temp_data:
        #search_term = character["real_name"].replace(" ", " ").lower()     

    #return jsonify({"error": f"Search with chosen date {start_date} not found."}), 404

#@app.route("/api/v1.0/<start>/<end>") #i think this is any start and to any end...within date range

if __name__ == "__main__":
    app.run(debug=True)
