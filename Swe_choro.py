#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 22:04:09 2022

@author: bjorn
"""

import json
import numpy as np
import pandas as pd
import plotly.express as px

kommuner = json.load(open('swe_geo.json', 'r'))

kommun_pop = pd.read_csv('pop.csv',
                         sep = ',',
                         thousands=' ')

kommun_pop['2021 antal'] = kommun_pop['2021 antal'].str.replace("[^\d.,e+-]","").astype(int)