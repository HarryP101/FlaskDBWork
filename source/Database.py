#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:22:16 2019

@author: Harry
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/log.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class CurrencyRates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True, nullable=False)
    base = db.Column(db.String(3), unique=True, nullable=False)
    rate = db.Column(db.Float, unique=True, nullable=False)


class Database:
    
    def __init__(self, databaseURL):
        self.dbURL = databaseURL
        db.drop_all() # For debugging purposes
        db.create_all()
    
    def Add(self, currencyRates):
        db.session.add(currencyRates)
    
    def Commit(self):
        db.session.commit()
        return
    
    def Load(self):
        # A function to load db from database URL into member variables of database
        return 