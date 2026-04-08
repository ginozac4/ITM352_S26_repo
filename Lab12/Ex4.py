# Name: Cassiddy Ginoza
# Date: Apr. 7, 2026

# get public license data from city of chicago's data portal

import pandas as pd
from sodapy import Socrata

# create a sodapy client to access the City of Chicago's Data Portal
client = Socrata("data.cityofchicago.org", None)

# Specify the JSON file for license data
json_file = "rr23-ymwb"

results = client.get(json_file, limit = 500)
# convert the results into a DataFrame for easier analysis
df = pd.DataFrame.from_records(results)

# print(df.head())

vehicles_and_fuel_sources = df[["public_vehicle_number","vehicle_fuel_source"]]
print("Public Vehicle Numbers and their Fuel Sources:")
# print(vehicles_and_fuel_sources.head())

vehicles_by_fuel_sources = vehicles_and_fuel_sources.groupby("vehicle_fuel_source").count()
print(vehicles_by_fuel_sources)