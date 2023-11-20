# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pandas as pd
import datetime as dt
#could it not have been working because i had more than one end?
##from matplotlib import style
##style.use('fivethirtyeight')
##import matplotlib.pyplot as plt
#################################################
# Database Setup
#################################################
# 1. import Flask
from flask import Flask
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)
# 3. Define what to do when a user hits the index route #why does this work only from another file?
@app.route("/")
def congrats():
    #print("Server received request for 'welcome' page...")
    return (
        f"Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii.<br/>"
        f"To help with your trip planning, here is a climate analysis about the area.<br/>" 
        f"The following sections will help accomplish this!<br/>"
        f"hope this is working<br/>"
        f"Things to consider (Routes) to help you plan:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )
# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    #print("Server received request for 'precipitation' page...")
    return "Welcome to my 'precipitation' page!"

@app.route("/api/v1.0/stations")
def stations():
    return "Look at these stations"

@app.route("/api/v1.0/tobs")
def tobs():
    return "Look at tobs"

#@app.route("/api/v1.0/stations")
#def start_end():
    #return "Look at these"

if __name__ == "__main__":
    app.run(debug=True)
