{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "from dateutil.relativedelta import relativedelta\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "measurement",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sqlalchemy\\util\\_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    209\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 210\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    211\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'measurement'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-829bb15cf80a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mBase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprepare\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mreflect\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m \u001b[0mMeasurement\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmeasurement\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m \u001b[0mStation\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstation\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sqlalchemy\\util\\_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    210\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    211\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 212\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    213\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    214\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__contains__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: measurement"
     ]
    }
   ],
   "source": [
    "engine = create_engine('sqlite:///hawaii.sqlite')\n",
    "\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect=True)\n",
    "\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station\n",
    "\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "\n",
    "# last 12 months variable\n",
    "last_twelve_months = '2016-08-23'\n",
    "\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    return (\n",
    "        f\"<p>Welcome to the Hawaii weather API!</p>\"\n",
    "        f\"<p>Usage:</p>\"\n",
    "        f\"/api/v1.0/precipitation<br/>Returns a JSON list of percipitation data for the dates between 8/23/16 and 8/23/17<br/><br/>\"\n",
    "        f\"/api/v1.0/stations<br/>Returns a JSON list of the weather stations<br/><br/>\"\n",
    "        f\"/api/v1.0/tobs<br/>Returns a JSON list of the Temperature Observations (tobs) for each station for the dates between 8/23/16 and 8/23/17<br/><br/>\"\n",
    "        f\"/api/v1.0/date<br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and 8/23/17<br/><br/>.\"\n",
    "        f\"/api/v1.0/start_date/end_date<br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and end date<br/><br/>.\"\n",
    "    )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# /api/v1.0/precipitation\n",
    "# Query for the dates and temperature observations from the last year.\n",
    "# Convert the query results to a Dictionary using date as the key and tobs as the value.\n",
    "# Return the JSON representation of your dictionary.\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    # Date 12 months ago\n",
    "    p_results = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date >= last_twelve_months).group_by(Measurement.date).all()\n",
    "    return jsonify(p_results)\n",
    "\n",
    "\n",
    "# /api/v1.0/stations\n",
    "# Return a JSON list of stations from the dataset.\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    s_results = session.query(Station.station, Station.name).all()\n",
    "    return jsonify(s_results)\n",
    "\n",
    "\n",
    "# /api/v1.0/tobs\n",
    "# Return a JSON list of Temperature Observations (tobs) for the previous year\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def tobs():\n",
    "    t_results = session.query(Measurement.date, Measurement.station, Measurement.tobs).filter(Measurement.date >= last_twelve_months).all()\n",
    "    return jsonify(t_results)\n",
    "\n",
    "\n",
    "# /api/v1.0/<start>\n",
    "# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.\n",
    "# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.\n",
    "@app.route(\"/api/v1.0/<date>\")\n",
    "def startDateOnly(date):\n",
    "    day_temp_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= date).all()\n",
    "    return jsonify(day_temp_results)\n",
    "\n",
    "\n",
    "# /api/v1.0/<start>/<end>\n",
    "# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.\n",
    "# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.\n",
    "@app.route(\"/api/v1.0/<start>/<end>\")\n",
    "def startDateEndDate(start,end):\n",
    "    multi_day_temp_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()\n",
    "    return jsonify(multi_day_temp_results)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
