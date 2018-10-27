from flask import Flask, render_template, jsonify
from flask_pymongo import MongoClient
import time
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from pprint import pprint
import pymongo
from pymongo import MongoClient
import json
from bson.json_util import dumps
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
from zipfile import ZipFile
import os
import time
import shutil
from datetime import datetime as dt
from pymongo import MongoClient
from flask_pymongo import PyMongo
#import scrape_metro
#import scrape_events

app = Flask(__name__, static_url_path='/static', template_folder='templates')

url = 'mongodb://admin:USCbootcamp2018@ds141633.mlab.com:41633/la_events'
client = MongoClient(url)
db = client['la_events']

app.config["MONGO_URI"] = "mongodb://admin:USCbootcamp2018@ds141633.mlab.com:41633/la_events"
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about_us")
def aboutus():
    return render_template("aboutus.html")

@app.route("/plot_1")
def plot_1():
   return render_template("plot.html")

@app.route("/la_bike_maps")
def bike_maps():
   return render_template("la_map.html")

@app.route("/bike_station")
def returnBike_station():
    jsonevents=[]
    collection = db.bike_station
    dbevents = collection.find()
    l = list(dbevents)
    for i in l:
      v = list(i.values())[1]
      jsonevents.append(
         {
          "Region" : v[0],
          "station_count" : v[1]      
         }
        )
    # print(jsonevents)
    return jsonify(jsonevents) 

@app.route("/day_week")
def returnDay_week():
    jsonevents=[]
    collection = db.day_week
    dbevents = collection.find()
    l = list(dbevents)
    for i in l:
      v = list(i.values())[1]
      jsonevents.append(
         {
          "Day_Of_Week" : v[0],
          "Region" : v[2],
          "Day_Of_Week_Number" : v[1],
          "trip_count" : v[3]
         }
        )
    # print(jsonevents)
    return jsonify(jsonevents)

@app.route("/day_week_normalized")
def returnDay_week_normalized():
    jsonevents=[]
    collection = db.day_week_normalized
    dbevents = collection.find()
    l = list(dbevents)
    for i in l:
      v = list(i.values())[1]
      jsonevents.append(
         {
          "Day_Of_Week" : v[0],
          "normalized_trip_count" : v[3],
          "Region" : v[2],
          "Day_Of_Week_Number" : v[1]
         }
        )
    # print(jsonevents)
    return jsonify(jsonevents)

@app.route("/events")
def events():
  jsonevents=[]                # list of jsons that will be used for return
  dbevents = collection.find() # collection
  l = list(dbevents)           # cast  to list for easier handling
  for i in l:                  # each i is a dictionary
    v = list(i.values())[1]    # get the values, the 2nd one has the info, hence [1]
    jsonevents.append(         # populate final list
       {
        "title" : v[3],
        "date"  : v[0],
        "location" : v[1],
        "read_more" : v[2]
       }
      )
  return jsonify(jsonevents)  # jsonify before returning otherwise it is a dict, so the client/browser would not know how to handle it

@app.route("/passholder")
def returnPassholder():
  jsonevents=[]
  collection = db.passholder
  dbevents = collection.find()
  l = list(dbevents)
  for i in l:
    v = list(i.values())[1]
    jsonevents.append(
       {
        "passholder_type" : v[0],
        "Region" : v[1],
        "trip_count" : v[2]
       }
      )
  # print(jsonevents)
  return jsonify(jsonevents)

@app.route("/passholder_normalized")
def returnPassholder_normalized():
  jsonevents=[]
  collection = db.passholder_normalized
  dbevents = collection.find()
  l = list(dbevents)
  for i in l:
    v = list(i.values())[1]
    jsonevents.append(
       {
        "passholder_type" : v[0],
        "Region" : v[1],
        "normalized_trip_count" : v[2]
       }
      )
  # print(jsonevents)
  return jsonify(jsonevents)

@app.route("/route_c_normalized")
def returnRoute_c_normalized():
  jsonevents=[]
  collection = db.route_c_normalized
  dbevents = collection.find()
  l = list(dbevents)
  for i in l:
    v = list(i.values())[1]
    jsonevents.append(
       {
        "trip_route_category" : v[0],
        "Region" : v[1],
        "normalized_trip_count" : v[2]
       }
      )
  # print(jsonevents)
  return jsonify(jsonevents)

@app.route("/routes")
def returnRoutes():
  jsonevents=[]
  collection = db.routes
  dbevents = collection.find()
  l = list(dbevents)
  for i in l:
    v = list(i.values())[1]
    jsonevents.append(
       {
        "trip_route_category" : v[0],
        "Region" : v[1],
        "trip_count" : v[2]
       }
      )
  # print(jsonevents)
  return jsonify(jsonevents)  

@app.route("/start_station")
def returnStart_station():
  jsonevents=[]
  collection = db.start_station
  dbevents = collection.find()
  l = list(dbevents)
  for i in l:
    v = list(i.values())[1]
    jsonevents.append(
       {
        "amount" : v[0],
        "address" : v[1],
        "location" : v[2],
        "start_lat" : v[3],
        "start_lon" : v[4],
        "end_lat" : v[5],
        "end_lon" : v[6]
       }
      )
  # print(jsonevents)
  return jsonify(jsonevents)


@app.route("/top30")
def return30():
  jsonevents=[]
  collection = db.top30
  dbevents = collection.find()
  l = list(dbevents)
  for i in l:
    v = list(i.values())[1]
    jsonevents.append(
       {
        "start_to_end" : v[0],
        "start_to_end_name" : v[1],
        "Region" : v[2],
        "start_lat" : v[3],
        "start_lon" : v[4],
        "end_lat" : v[5],
        "end_lon" : v[6],
        "trip_id" : v[7],
       }
      )
  # print(jsonevents)
  return jsonify(jsonevents)

@app.route("/year_month")
def returnYear_month():
  jsonevents=[]
  collection = db.year_month
  dbevents = collection.find()
  l = list(dbevents)
  for i in l:
    v = list(i.values())[1]
    jsonevents.append(
       {
        "Year-Month" : v[0],
        "Region" : v[1],
        "trip_count": v[2]
       }
      )
  # print(jsonevents)
  return jsonify(jsonevents)

@app.route("/year_month_normalized")
def returnYear_month_normalized():
  jsonevents=[]
  collection = db.year_month_normalized
  dbevents = collection.find()
  l = list(dbevents)
  for i in l:
    v = list(i.values())[1]
    jsonevents.append(
       {
        "Year-Month" : v[0],
        "Region" : v[1],
        "normalized_trip_count" : v[2]
       }
      )
  # print(jsonevents)
  return jsonify(jsonevents)
# @app.route("/scrape")
# def scrape():
#   executable_path = {'executable_path': '/anaconda3/bin/chromedriver'}
#   browser = Browser('chrome', **executable_path, headless=True)

#   url = "https://www.timeout.com/los-angeles/things-to-do/october-events-calendar"
#   browser.visit(url)

#   html = browser.html
#   soup = BeautifulSoup(html, 'html.parser')
#   browser.quit()

#   complete = soup.find_all('div', class_='card-content xs-col-12 sm-col-8 sm-pl5')

#   _events = []

#   for item in complete:
#       _event = {}
#       try:
#           _event['title'] = item.find('a', class_='xs-text-charcoal decoration-none title-underline theme-title-underline').text.strip()
#       except:
#           _event['title'] = np.nan
          
#       try:    
#           _event['location'] = item.find('span', class_='bold sm-text-8 xs-text-9 xs-line-height-10 xs-inline-block xs-mr1').text.strip()
#       except:
#           _event['location'] = np.nan
          
#       try:
#           _event['date'] = item.find('time', class_='bold sm-text-8 xs-text-9 xs-line-height-10 xs-inline-block xs-mr1').text.strip()
#       except:
#           np.nan
      
#       try:
#           _event['read_more'] = f"https://www.timeout.com/{item.find('a', class_='amp-btn-secondary bold xs-px5 xs-py2 xs-text-7 xs-fill-white xs-border rounded xs-inline-block decoration-none xs-border-black xs-hover--border-black-dark xs-text-black xs-hover--text-black-dark xs-hover--box-shadow-black-secondary')['href']}"
#       except:
#           _event['read_more'] = np.nan
          
#       _events.append(_event)

#       df_1 = pd.DataFrame(_events)
#       print(df_1.head())

#    #    mongo_uri = 'mongodb://localhost:27017'
#     # conn = MongoClient(mongo_uri)
#     # db = conn.mydb
#     # collection = db.mydf

#   db.drop_collection(collection)

#   cols = ['title', 'date', 'location', 'read_more']

#   for index, row in df_1.iterrows():
#     collection.insert_one({str(index): list(row.values)})
#     # print(str(index), list(row.values))
#     #return redirect("/", code=302)

# # while True:
# #   time.sleep(86400)
# #   scrape_events.timeout_events()

if __name__ == "__main__":
  app.run(debug=True)
