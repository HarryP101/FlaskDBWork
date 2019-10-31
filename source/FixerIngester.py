#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:46:25 2019

@author: Harry
"""

import requests
from requests.exceptions import HTTPError
from .Database import db, CurrencyRates, Database
import datetime

class FixerIngester:
    
    
    def __init__(self, database, accessKey):
    
        self.MY_ACCESS_KEY=accessKey
        self.currencyRates = {}
        self.database = database
    
    def Ingest(self):
        
        for url in ['http://data.fixer.io/api/latest?access_key={}&symbols=USD,AUD,CAD,PLN,MXN&format=1'.format(self.MY_ACCESS_KEY)]:
            try:
                response = requests.get(url)
                response.raise_for_status()
            except HTTPError as http_err:
                print('HTTP error occurred: {}'.format(http_err))
            except Exception as err:
                print('Other error occurred: {}'.format(err))
            else:
                print('Success!')
                print(response.json())
                self.currencyRates = response.json()


    def Add(self):
        date = datetime.datetime.strptime(self.currencyRates['date'], '%Y-%m-%d')
        cRates = CurrencyRates(date=date, base=self.currencyRates['base'], rate=self.currencyRates['rates']['USD'])
        self.database.Add(cRates)
        return
    
    
    def GetCurrencyRates(self, date):
        url = 'http://data.fixer.io/api/{}?access_key={}&symbols=USD,AUD,CAD,PLN,MXN&format=1'.format(self.MY_ACCESS_KEY, date)
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print('HTTP error occurred: {}'.format(http_err))
        except Exception as err:
            print('Other error occurred: {}'.format(err))
        else:
            print('Success!')
            return response.json()
        

if __name__ is "__main__":
    myAccessKey = "c22ba25cbec7756b0aa7dfdf7bb70393"
    database = Database('sqlite:////tmp/log.db')
    database.Load()
    fixerIngester = FixerIngester(database, myAccessKey)
    fixerIngester.Ingest() # Gets currency data from fixer, stores as member variable
    fixerIngester.Add() # Adds to the database
    database.Commit() # Commit changes