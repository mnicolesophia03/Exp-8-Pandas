# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:27:53 2019

@author: Nicole Sophia
"""

import pandas as pd
cars = pd.read_csv('cars.csv')

print(aqd.iloc[0:5:, range(0,11,2)])
print('--------------------------')

print(aqd[aqd['Model']=='Mazda RX4'])
print('--------------------------')

print(aqd.loc[aqd['Model']=='Camaro Z28', ['Model', 'cyl']])
print('--------------------------')

print(aqd.loc[aqd['Model']=='Mazda RX4 Wag', ['cyl', 'gear']])
print(aqd.loc[aqd['Model']=='Ford Pantera L', ['cyl', 'gear']])
print(aqd.loc[aqd['Model']=='Honda Civic', ['cyl', 'gear']])