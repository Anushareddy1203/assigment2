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
    
def plotting_data(indicator_name):
    """This function takes indicator name as argument, It plots the bar graph for the dataframe and
    returns the filtered dataframe for the indicator with given countries and years"""



    if indicator_name == "Population growth (annual %)":
        label = "Percentage (%)"
    elif indicator_name == "CO2 emissions (kg per 2015 US$ of GDP)":
        label = "kg per 2015 US$ of GDP"

    # filter the dataframe with given countries and indicator name and set the index as Country Name.
    selected_data = main_dataframe[
        (main_dataframe["Country Name"].isin(countries))
        & (main_dataframe["Indicator Name"] == indicator_name)
    ].set_index("Country Name")

    # filter the dataframe with given years and reset the index
    refined_df = selected_data.loc[:, years].reset_index()

    

    refined_df.set_index("Country Name").plot.bar(
        rot=0, xlabel="Countries", ylabel=label, title=indicator_name
    )

    return refined_df


# driver code for plotting_data function
collected_data = plotting_data(indicator_name="Population growth (annual %)")
plotting_data(indicator_name="CO2 emissions (kg per 2015 US$ of GDP)")


def mean_stats():
    """This function plots the bar graph for the mean of the population growth with the help of
    pandas statistical function mean()"""

    # mean of the population growth
    mean_series = collected_data.mean(numeric_only=True)
    mean_data = pd.DataFrame({"Years": years, "mean": mean_series})
    mean_data.set_index("Years").plot.bar(
        rot=0, title="Annual mean of the population growth"
    )
    
