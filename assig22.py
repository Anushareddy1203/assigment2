# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 04:26:49 2022

@author: anush
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# initial data for analysis

# Countries and years for analysis
countries = ["India", "Canada", "China", "Pakistan", "United Kingdom", "Australia"]
years = ["2005", "2008", "2010", "2012", "2015", "2018"]

# read the csv file
main_dataframe = pd.read_csv("C:/Users/anush/OneDrive/Desktop/World_bank_data.csv")
