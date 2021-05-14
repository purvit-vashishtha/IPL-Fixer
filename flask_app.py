#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:31:16 2021

@author: purvit
"""

from flask import Flask, render_template, request
import pickle
import numpy as np
from flasgger import Swagger

filename = 'score_pred_model.pkl'
regressor = pickle.load(open(filename,"rb"))

app = Flask(__name__)
Swagger(app)

@app.route('/')
def welcome():
    return"Welcome"

@app.route('/predict', methods= ["Get"])
def prediction():
    """IPL Score Prediction App
    Using previous data to predict.
    ---
    parameters:
        - name: overs
          in: query
          type: number
          required: true
        - name: runs
          in: query
          type: number
          required: true
        - name: wickets
          in: query
          type: number
          required: true
        - name: runs_in_prev_5 
          in: query
          type: number
          required: true
       - name: wickets_in_prev_5 
          in: query
          type: number
          required: true
     
    responses:
          200:
              description: The Output values
    """
    temp_arr = list()
    
    if request.method == "POST":
        batting_team  = request.form("batting_team")
        
        if batting_team == "Delhi Daredevils":
            temp_arr = temp_arr + [1,0,0,0,0,0,0,0]
        
        elif batting_team == "Chennai Super Kings":
            temp_arr = temp_arr + [0,1,0,0,0,0,0,0]
        
        elif batting_team == "Rajasthan Royals":
            temp_arr = temp_arr + [0,0,1,0,0,0,0,0]
            
        elif batting_team == "Kings XI Punjab":
            temp_arr = temp_arr + [0,0,0,1,0,0,0,0]
            
        elif batting_team == "Mumbai Indians":
            temp_arr = temp_arr + [0,0,0,0,1,0,0,0]
            
        elif batting_team == "Sunrisers Hyderabad":
            temp_arr = temp_arr + [0,0,0,0,0,1,0,0]
        
        elif batting_team == "Kolkata Knight Riders":
            temp_arr = temp_arr + [0,0,0,0,0,0,1,0]
        
        elif batting_team == "Royal Challengers Bangalore":
            temp_arr = temp_arr + [0,0,0,0,0,0,0,1]
            
        
        bowling_team = request.form['bowling-team']
        if bowling_team == "Delhi Daredevils":
            temp_arr = temp_arr + [1,0,0,0,0,0,0,0]
        
        elif bowling_team == "Chennai Super Kings":
            temp_arr = temp_arr + [0,1,0,0,0,0,0,0]
        
        elif bowling_team == "Rajasthan Royals":
            temp_arr = temp_arr + [0,0,1,0,0,0,0,0]
            
        elif bowling_team == "Kings XI Punjab":
            temp_arr = temp_arr + [0,0,0,1,0,0,0,0]
            
        elif bowling_team == "Mumbai Indians":
            temp_arr = temp_arr + [0,0,0,0,1,0,0,0]
            
        elif bowling_team == "Sunrisers Hyderabad":
            temp_arr = temp_arr + [0,0,0,0,0,1,0,0]
        
        elif bowling_team == "Kolkata Knight Riders":
            temp_arr = temp_arr + [0,0,0,0,0,0,1,0]
        
        elif bowling_team == "Royal Challengers Bangalore":
            temp_arr = temp_arr + [0,0,0,0,0,0,0,1]
        
        
    overs = float(request.form['overs'])
    runs = int(request.form['runs'])
    wickets = int(request.form['wickets'])
    runs_in_prev_5 = int(request.form['runs_in_prev_5'])
    wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
    temp_arr = temp_arr + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
    data = np.array([temp_arr])
    my_prediction = int(regressor.predict(data)[0])
    
    return str(my_prediction)


    
if __name__=="__main__":
   app.run(debug=True)