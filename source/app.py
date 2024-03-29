#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:05:04 2019

@author: Harry
"""
from flask import Flask
from FixerIngester import FixerIngester
myAccessKey = "c22ba25cbec7756b0aa7dfdf7bb70393"
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'


@app.route('/GetCurrencyRates/<date>')
def GetCurrencyRatesForDate(date):
    currencyRates = FixerIngester.GetCurrencyRates(date, myAccessKey)
    return currencyRates