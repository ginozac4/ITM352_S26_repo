# Name: Cassiddy Ginoza
# Date: March 24, 2026

#read a json file of taxi trip data and create a dataframe.
#calculate the median fare

import json
import pandas as pd

taxi_df = pd.read_json("taxi_trips.json")
print(taxi_df.describe()) #calculates the statistics for the fare column since it is the only column with numerical data

# print(taxi_df.head()) #prints the first 5 rows of the dataframe to see what the data looks like

median_fare = taxi_df["fare"].median()
print(f"Median fare: ${median_fare:.2f}")