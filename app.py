import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template


username = 'postgres'
password = 'postgres'
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/Project_2')



Base = automap_base()

Base.prepare(engine, reflect=True)

Superbowls = Base.classes.superbowl


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 



@app.route("/")
def IndexRoute():
    

    webpage = render_template("index.html")
    return webpage
@app.route("/winlose")
def WinnersRoute():



    webpage = render_template("winlose.html")
    return webpage
@app.route("/attendance")
def LosersRoute():



    webpage = render_template("attendance.html")
    return webpage
@app.route("/map")
def MapRoute():

    webpage = render_template("map.html")
    return webpage
@app.route("/dictionary")
def DictionaryRoute():

    session = Session(engine)

    results = session.query(Superbowls.sb, Superbowls.attendance, Superbowls.winner, Superbowls.winning_pts, Superbowls.loser, Superbowls.losing_pts, Superbowls.mvp, Superbowls.stadium, Superbowls.city_state, Superbowls.lat, Superbowls.lng).all()

    session.close()


    all_sbs = []
    for sb, attendance, winnner, winning_pts, loser, losing_pts, mvp, stadium, city_state, lat, lng in results:
        superbowl_dict = {}
        superbowl_dict["Superbowl"] = sb
        superbowl_dict["Attendance"] = attendance
        superbowl_dict["Winner"] = winnner
        superbowl_dict["Winning points"] = winning_pts
        superbowl_dict["Loser"] = loser
        superbowl_dict["Losing points"] = losing_pts
        superbowl_dict["Most Valuable Player"] = mvp
        superbowl_dict["Stadium"] = stadium
        superbowl_dict["Citystate"] = city_state
        superbowl_dict["Latitude"] = lat
        superbowl_dict["Longitude"] = lng
        all_sbs.append(superbowl_dict)

    return jsonify(all_sbs)

@app.route("/mapData")
def mapRoute():

    session = Session(engine)

    map_results = session.query(Superbowls.sb, Superbowls.city_state,
    Superbowls.lat, Superbowls.lng, Superbowls.winner, Superbowls.loser,
    Superbowls.winning_pts, Superbowls.losing_pts).all()

    session.close()

# Create dictionary of map coordinates

    coordinates = []

    for sb, city_state, lat, lng, winner, loser, winning_pts, losing_pts in map_results:
        coordinates_dict = {}
        coordinates_dict["superbowl"] = sb
        coordinates_dict["city_state"] = city_state
        coordinates_dict["lat"] = lat
        coordinates_dict["long"] = lng
        coordinates_dict["winner"] = winner
        coordinates_dict["loser"] = loser
        coordinates_dict["winner_pts"] = winning_pts
        coordinates_dict["loser_pts"] = losing_pts



        coordinates.append(coordinates_dict)


    return jsonify(coordinates)




if __name__ == '__main__':
    app.run(debug=True)







