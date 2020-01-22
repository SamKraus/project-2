# Import the functions we need from flask
import numpy as np
import pandas as pd
from flask import Flask
from flask import render_template 
from flask import jsonify

# Import the functions we need from SQL Alchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
#############################################
# Datatbase Setup
#############################################

username = 'postgres'
password = 'chicago1023'
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/Project_2')

connection = engine.connect()

#reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Superbowls = Base.classes.superbowl


##############################################
# Flask Setup
#########################################
             
# This statement is required for Flask to do its job. 
# Think of it as chocolate cake recipe. 
app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] =0      
#########################################

@app.route("/")
def welcome():
    """list all routes"""
   
#     return(
#         f"Available Routes:<br/>"
#         f"/api/v1.0/index</br>"
#         f"/api/v1.0/other<br/>"
#         f"/api/v1.0/data<br/>"
#         f"/api/v1.0/map<br/>"
#         f"/api/v1.0/jsonified"      
#  )

    webpage = render_template("map.html")
    return webpage
###################################################

# Here's where we define the various application routes ...
@app.route("/index")
def IndexRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''

    webpage = render_template("other.html")
    return webpage
#################################################

@app.route("/other")
def OtherRoute():
    ''' This function runs when the user clicks the link for the other page.
        Note that the html file must be located in a folder called templates. '''

    # Note that this call to render template passes in the title parameter. 
    # That title parameter is a 'Shirley' variable that could be called anything 
    # we want. But, since we're using it to specify the page title, we call it 
    # what we do. The name has to match the parameter used in other.html. 
    webpage = render_template("other.html", title_we_want="Shirley")
    return webpage

# ###########################################################
@app.route("/data")
def DataRoute():
    session = Session(engine)
    # Query all passengers
    results = session.query(Superbowls.sb).all()
    session.close()
    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))
    return jsonify(all_names)

    ''' This function runs when the user clicks the link for the other page.
        Note that the html file must be located in a folder called templates. '''

    # Note that this call to render template passes in the title parameter. 
    # That title parameter is a 'Shirley' variable that could be called anything 
    # we want. But, since we're using it to specify the page title, we call it 
    # what we do. The name has to match the parameter used in other.html. 
   
#################################################################


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



    # ''' This function returns a simple message, just to guarantee that
    # the Flask server is working. '''


###################################################
#   Return the jsonified version of the dictionary
###################################################

@app.route("/jsonified")

def jsonified():

    session = Session(engine)

    results = []

    for s in session.query(Superbowls).all():
        results.append({'sb': s.sb, 'attendance': s.attendance, 
        'winner': s.winner, 'winning pts': s.winning_pts,'loser': s.loser,
        'losing pts': s.losing_pts, 'mvp': s.mvp, 'stadium': s.stadium,
        'city, state': s.city_state, 'lat': s.lat, 'long': s.lng})

    print(results)


    session.close()

    return jsonify(results)


#########################################################
# This statement is required for Flask to do its job. 
# Think of it as chocolate cake recipe. 
#########################################################
if __name__ == '__main__':
    app.run(debug=True)