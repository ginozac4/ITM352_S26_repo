# Name: Cassiddy Ginoza
# Date: March 24, 2026

import pandas as pd
import csv

df_homes = pd.read_csv("homes_data.csv")

# convert columns to appropriate data types

df_big_properties = df_homes[df_homes["units"] >= 500]
df_big_properties = df_big_properties.drop(columns = ["id", "easement"])
df_big_properties["sale_price"] = pd.to_numeric(df_big_properties["sale_price"], errors="coerce")
df_big_properties["land_sqft"] = pd.to_numeric(df_big_properties["land_sqft"], errors="coerce")
df_big_properties["gross_sqft"] = pd.to_numeric(df_big_properties["gross_sqft"], errors="coerce")

# drop rows with missing values in the numeric columns and drop duplicates
df_big_properties = df_big_properties.dropna()
df_big_properties = df_big_properties.drop_duplicates()

# print out first 10 rows of the cleaned dataframe
#print(df_big_properties.head(10))

df_big_properties = df_big_properties[df_big_properties["sale_price"] > 0]

#calculate the average sale price per square foot for the big properties
average_price = df_big_properties["sale_price"].mean()
print(df_big_properties.head(10))
print(f"The mean sales price for the big properties is ${average_price:.2f}")