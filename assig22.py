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

def countries_years(file_name):
    """This function takes a filename as argument, reads a dataframe in World bank format
    and returns two dataframes:one with years as columns and one with countries as columns."""

    # read the csv file
    read_data = pd.read_csv(file_name)

    # # Get unique values of Country Name and set as columns of the dataframe and transpose the dataframe
    # country_columns = (
    #     pd.DataFrame({"Country Name": read_data["Country Name"].unique()})
    #     .set_index("Country Name")
    #     .transpose()
    # )

    # # Get unique vales of Year set as index and transpose the dataframe.

    # years_columns = (
    #     pd.DataFrame({"Year": read_data.columns[4:]}).set_index("Year").transpose()
    # )
    
def countries_years(file_name):
    """This function takes a filename as argument, reads a dataframe in World bank format
    and returns two dataframes:one with years as columns and one with countries as columns."""

    # read the csv file
    read_data = pd.read_csv(file_name)

    # # Get unique values of Country Name and set as columns of the dataframe and transpose the dataframe
    # country_columns = (
    #     pd.DataFrame({"Country Name": read_data["Country Name"].unique()})
    #     .set_index("Country Name")
    #     .transpose()
    # )

    # # Get unique vales of Year set as index and transpose the dataframe.

    # years_columns = (
    #     pd.DataFrame({"Year": read_data.columns[4:]}).set_index("Year").transpose()
    # )
