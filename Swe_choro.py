#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 22:04:09 2022

@author: bjorn
"""

import json
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='chromium'


lan = json.load(open('swe_geo.json', 'r'))

kommun_pop = pd.read_csv('lan_1749-2020.csv',
                         sep = ',',
                         thousands=' ')

#kommun_pop = kommun_pop.rename(columns = {'Kommun':'landskap'})
#kommuner['features'][0]['properties']['landskap']

for i in lan['features']:
    i['Län'] = i['properties']['landskap']



plt = px.choropleth(kommun_pop, 
                    locations= 'Län',
                    geojson= lan,
                    color = '2020')

plt.show()

