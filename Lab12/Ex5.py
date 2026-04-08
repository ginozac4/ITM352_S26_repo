# Name: Cassiddy Ginoza
# Date: Apr. 7, 2026

# get a JSON file from the City of Chicago and analyze driver types

import pandas as pd
import requests

# create a REST query to get the JSON file for data types

search_results = requests.get("https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type")
 # treating it like a database

results_json = search_results.json()
print(type(results_json))
print("Driver types and their Counts: ")
print(results_json)

# convery the JSON results to a DataFrame for easier analysis
results_df = pd.DataFrame(results_json)
results_df.columns = ["driver_type","count"]
results_df = results_df.set_index("driver_type")

print("\nDriver Types and their Counts (DataFrame):")
print(results_df)