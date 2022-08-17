import json
import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pylab as pl
from numpy.polynomial.polynomial import polyfit
from scipy.stats import pearsonr



def TempWithin(path_name, file_name, heat_data):
    if file_name.endswith("geojson"):
        planimetric_df = gpd.read_file(r"{}\{}".format(path_name, file_name)) # Read file
        temp_within_planimetric = gpd.sjoin(heat_data, planimetric_df, how="inner") #Find datapoints in heat data that are within the planimetric feature
        degrees='F' # Convert C to F
        if degrees == 'C':
            pass
        elif degrees == 'F':
            temp_within_planimetric['ST_B10'] = [(x * 9/5) + 32 for x in temp_within_planimetric['ST_B10']]
        else:
            raise Exception('Invalid Temperature Scale. Must be C or F.')
             
    print("NYC Average Temperature: 97.7 +/- 6.4 F\nAverage Temperature of {}: {} +/- {} F".format(file_name, temp_within_planimetric.ST_B10.mean(), temp_within_planimetric.ST_B10.std()))