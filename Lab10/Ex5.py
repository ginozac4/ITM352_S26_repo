# Name: Cassiddy Ginoza
# Date: March 24, 2026

# Read in a csv file of homes data and create a dataframe.
# do filtering and statistics on the data

import pandas as pd
import csv

df_homes = pd.read_csv("homes_data.csv")

#print out the shape of the dataframe and first few rows
shape = df_homes.shape
print(f"The homes data has {shape[0]} rows and {shape[1]} columns.")
print(df_homes.head(10)) 

#select only the properties with 500 or more units

df_big_properties = df_homes[df_homes["units"] >= 500]
df_big_properties = df_big_properties.drop(columns = ["id", "easement"])
print(df_big_properties.head(10))