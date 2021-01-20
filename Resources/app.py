import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, request

engine = create_engine('sqlite:///hawaii.sqlite', connect_args={'check_same_thread': False})

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"<p>Hawaii Weather</p>"
        f"/api/v1.0/precipitation<br/>Precipitation Data<br/><br/>"
        f"/api/v1.0/stations<br/>Stations<br/><br/>"
        f"/api/v1.0/tobs<br/>Temperature Data<br/><br/>"
        f"/api/v1.0/start_date<br/>Enter ?start_date1= followed by date you want in m/d/yyyy format<br/><br/>."
        f"/api/v1.0/start_date/end_date<br/>Enter ?start_date1= followed by date you want in m/d/yyyy format then &end_date1 = in the same way<br/><br/>."
)

@app.route("/api/v1.0/precipitation")
def prec():
    precdata = session.query(Measurement.date,func.SUM(Measurement.prcp)).filter(Measurement.date >= 8/23/2016).group_by(Measurement.date).all()
    return jsonify(precdata)

@app.route("/api/v1.0/stations")
def stations():
    stationsdata = session.query(Station.station, Station.name).all()
    return jsonify(stationsdata)

@app.route("/api/v1.0/tobs")
def temp():
    tempdata = session.query(Measurement.station, Measurement.tobs, Measurement.date).filter(Measurement.date >= 8/23/2016).all()
    return jsonify(tempdata)

@app.route("/api/v1.0/start_date",methods=['GET', 'POST'])
def temp2():
    start_date1 = request.args.get('start_date1')
    tempdata = session.query(func.MIN(Measurement.tobs), func.MAX(Measurement.tobs), func.AVG(Measurement.tobs)).filter(Measurement.date >= start_date1).all()
    return jsonify(tempdata)

@app.route("/api/v1.0/start_date/end_date",methods=['GET', 'POST'])
def temp3():
    start_date1 = request.args.get('start_date1')
    end_date1 = request.args.get('end_date1')
    tempdata = session.query(func.MIN(Measurement.tobs), func.MAX(Measurement.tobs), func.AVG(Measurement.tobs)).filter(Measurement.date >= start_date1).filter(Measurement.date <= end_date1).all()
    return jsonify(tempdata)

if __name__ == "__main__":
    app.run(debug=True)
