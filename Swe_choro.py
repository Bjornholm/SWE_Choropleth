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
#lan['features'][0]['properties']['name']
# d = 1
# for i in lan['features']:
#     print(i['properties']['landskap'] + " {}".format(d))
#     d = d+ 1

plt = px.choropleth(kommun_pop, 
                    geojson= lan,
                    locations= 'Län',
                    featureidkey='properties.name',
                    color = '2020',
                    hover_name = 'Län',
                    hover_data = ['2020'],
                    title = 'Sverige population per län')

plt.update_geos(fitbounds="locations", visible=False)
plt.show()