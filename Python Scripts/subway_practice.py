# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:14:37 2015

@author: Damian of Brooklyn
"""
"""Subway data P2"""

import pandas
import pandasql

subway_data = pandas.read_csv('C:\Users\Damian of Brooklyn\.spyder2\weather_underground.csv')


x = pandasql.sqldf("SELECT sum(rain) FROM subway_data;",globals())
print x['sum(rain)'][0] 

y = pandasql.sqldf("SELECT fog, max(maxtempi) FROM subway_data",globals())
print y['max(maxtempi)'][0]

z = pandasql.sqldf("SELECT avg(maxtempi) FROM subway_data WHERE cast(strftime('%w', date) as integer) < 2",globals())
print z['avg(maxtempi)'][0]

a = pandasql.sqldf("SELECT rain, avg(mintempi) FROM subway_data WHERE mintempi > 55",globals())
print a['avg(mintempi)'][0]

"""
turnstile_data = pandas.read_csv('C:\Users\Damian of Brooklyn\\turnstile_110528.csv')
print turnstile_data

better_turnstile_data = pandas.read_csv('C:\Users\Damian of Brooklyn\.spyder2\solution_turnstile_110528.csv')
print better_turnstile_data
"""

import csv
with open('C:\Users\Damian of Brooklyn\\turnstile_110528.csv')