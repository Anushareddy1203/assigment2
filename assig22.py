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

    # set the index as Country Name and transpose the dataframe and get the columns data
    country_columns = read_data.set_index("Country Name").transpose()

    # get the columns data from index 3
    columns_data = read_data.columns[3:]

    # set the index as Country Name and filter the dataframe with given columns data
    years_columns = read_data.set_index("Country Name")
    years_columns = years_columns.loc[:, columns_data]

    return country_columns, years_columns


country_as_columns, years__as_columns = countries_years(
    file_name="C:/Users/anush/OneDrive/Desktop/World_bank_data.csv"
)
print(country_as_columns, years__as_columns)


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


# driver code for mean_stats function
mean_stats()


def plot_corr(country_name):
    """This function takes the Country Name as argument and cross compare
    the correlations between different indicators of the Country and plot the heatmap"""

    # filter the dataframe with given country name
    country_data = main_dataframe[main_dataframe["Country Name"] == country_name]

    # list of indicators for the country
    indicator_names = [
        "Urban population",
        "Population, total",
        "CO2 emissions (kt)",
        "Forest area (sq. km)",
        "Agricultural land (sq. km)",
        "Cereal yield (kg per hectare)",
    ]

    # set the index as Indicator Name and filter the dataframe with given indicator names and years
    country_data_indicator = country_data.set_index("Indicator Name")

    # extract the data for the given years and indicator names and transpose the dataframe
    extracted_data_t = country_data_indicator.loc[indicator_names, years].transpose()
    

    # plot the heatmap for the correlation between different indicators
    plt.title(country_name, fontsize=15)
    sns.heatmap(extracted_data_t.corr(), linecolor='white',
                linewidths=0.1, annot=True, cmap="Accent")
    return extracted_data_t


plot_corr("India")
plot_corr("United Kingdom")
