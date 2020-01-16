# Import the functions we need from flask
#import psycopg2
#import sys
import numpy as numpy
import pandas as pd 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template



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

data = pd.read_sql('select * from superbowl', connection)
session = Session(engine)

results = []

for s in session.query(Superbowls).all():
    results.append({'sb': s.sb, 'attendance': s.attendance, 'winner': s.winner,
    'winning pts': s.winning_pts,
    'loser': s.loser, 'losing pts': s.losing_pts, 'mvp': s.mvp, 'stadium': s.stadium, 'city, state': s.city_state,
    'lat': s.lat, 'long': s.lng})

print(results)

session.close()

##########################################
# Flask Setup
#########################################

# This statement is required for Flask to do its job. 
# Think of it as chocolate cake recipe. 
app = Flask(__name__)

@app.route("/")
def welcome():
    """list all routes"""
    return render_template("index.html", sb=results[5])
    # return(
    #     f"Available Routes:<br/>"
    #     f"/api/v1.0/home<br/>"
    #     f"/api/v1.0/superbowls<br/>"
    #     f"/api/v1.0/dict<br/>"
    #     f"/api/v1.0/test<br/>"
  f"/api/v1.0/jsonified"
    # )


# # Here's where we define the various application routes ...
# @app.route("/")
# def IndexRoute():
#     ''' This function runs when the browser loads the index route. 
#         Note that the html file must be located in a folder called templates. '''

#     webpage = render_template("index.html")
#     return webpage

# @app.route("/other")
# def OtherRoute():
#     ''' This function runs when the user clicks the link for the other page.
#         Note that the html file must be located in a folder called templates. '''

#     # Note that this call to render template passes in the title parameter. 
#     # That title parameter is a 'Shirley' variable that could be called anything 
#     # we want. But, since we're using it to specify the page title, we call it 
#     # what we do. The name has to match the parameter used in other.html. 
#     webpage = render_template("other.html", title_we_want="Shirley")
#     return webpage

@app.route("/test")
def TestRoute():
    ''' This function returns a simple message, just to guarantee that
        the Flask server is working. '''

    return "This is the test route!"

# @app.route("/dictionary")
# def DictionaryRoute():
#     ''' This function returns a jsonified dictionary. Ideally we'd create 
#         that dictionary from a database query. '''

#     dict = { "Tequila": 10,
#              "Beer": 2,
#              "Red Wine": 8,
#              "White Wine": 1}
    
#     return jsonify(dict) # Return the jsonified version of the dictionary


@app.route("/jsonified")
def jsonified():
    return jsonify(results)


# @app.route("/dict")
# def DictRoute():
#     ''' This seems to work in the latest versions of Chrome. But it's WRONG to
#         return a dictionary (or any Python-specific datatype) without jsonifying
#         it first! '''        

#     dict = { "one": 1,
#              "two": 2,
#              "three": 3}
    
#     return dict # Don't return a dictionary! 


# # This statement is required for Flask to do its job. 
# # Think of it as chocolate cake recipe. 
# if __name__ == '__main__':
#     app.run(debug=True)