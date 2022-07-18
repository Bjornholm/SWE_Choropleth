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
from dash import Dash, dcc, html, Input, Output

pio.renderers.default='chromium'

lan = json.load(open('swe_geo.json', 'r'))

kommun_pop = pd.read_csv('lan_1749-2020.csv',
                         sep = ',',
                         thousands=' ')

year_columns = kommun_pop.columns[1:]
#mapping years with data to linear index
year_dict = {}
i=1
for y in year_columns:
    year_dict.update({i :y })
    i +=1

#Dash interactive elements 
#see https://plotly.com/python/mapbox-county-choropleth/

app = Dash(__name__)
app.layout = html.Div([
    html.H4('Population density per region Sweden'),
    html.P("Choose a year:"),
#TODO rotate text on slider, update on value change, not mouse release
    dcc.Slider(0,55,
               step=None,
               marks = year_dict,
               value=1,id="year"),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    Input("year", "value"))
def display_choropleth(year):

    fig = px.choropleth(kommun_pop, 
                    geojson= lan,
                    locations= 'Län',
                    featureidkey='properties.name',
                    color = year_dict[year],
                    hover_name = 'Län',
                    hover_data = [year_dict[year]],
                    title = 'Sverige population per län')
    fig.update_geos(fitbounds="locations", visible=True)
    return fig
app.run_server(debug=True)
